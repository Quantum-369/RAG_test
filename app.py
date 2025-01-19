from flask import Flask, request, jsonify, send_from_directory, render_template
from crawler import WebCrawler
from main import EmbeddingManager, generate_embeddings_with_batching, preprocess_markdown
import os
import logging
from openai import OpenAI
import numpy as np
from supabase import create_client
from collections import deque
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize OpenAI and Supabase clients
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
supabase = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))

app = Flask(__name__, static_url_path='', static_folder='static')

embedding_manager = EmbeddingManager()
crawler = WebCrawler()

# Initialize a conversation memory store
conversation_memory = {}
MAX_MEMORY = 5

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route("/api/process-url", methods=["POST"])
def process_url():
    try:
        data = request.get_json()
        url = data.get("url")
        is_sitemap = data.get("is_sitemap", False)
        persist_embeddings = data.get("persist_embeddings", False)

        # Create new session
        session_id = embedding_manager.create_session()

        # Crawl content using sync methods
        if is_sitemap:
            file_path = crawler.crawl_sitemap_sync(url)
            status_update("Crawled sitemap successfully")
        else:
            file_path = crawler.crawl_single_url_sync(url)
            status_update("Crawled URL successfully")

        # Process content
        chunks = preprocess_markdown(file_path)
        status_update("Preprocessed content into chunks")

        # Generate embeddings
        embeddings = generate_embeddings_with_batching(chunks)
        status_update("Generated embeddings")

        # Store embeddings
        embedding_manager.store_embeddings_in_supabase(embeddings, not persist_embeddings)
        status_update("Stored embeddings in database")

        return jsonify({
            "success": True,
            "session_id": session_id,
            "message": "Processing completed successfully"
        })

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")
        session_id = data.get("session_id", "default")

        # Initialize memory for new sessions
        if session_id not in conversation_memory:
            conversation_memory[session_id] = deque(maxlen=MAX_MEMORY)

        # Get embeddings for the user's question
        question_embedding = client.embeddings.create(
            model="text-embedding-3-small",
            input=user_message
        ).data[0].embedding

        # Query for relevant context
        query = supabase.rpc(
            'match_embeddings_v2',
            {
                'query_embedding': question_embedding,
                'similarity_threshold': 0.0,
                'match_count': 5
            }
        ).execute()

        if not query.data:
            return jsonify({
                "success": True,
                "response": "I don't have enough information in my database to answer that question."
            })

        # Extract contexts
        contexts = [item['text'] for item in query.data]
        context_text = "\n\n".join(contexts)

        # Get conversation history
        conversation_history = list(conversation_memory[session_id])
        history_text = "\n".join([f"User: {h['user']}\nAssistant: {h['assistant']}" 
                                for h in conversation_history])

        # Create prompt with conversation history
        system_prompt = (
            "You are a helpful assistant. Use the provided context and conversation history to answer the user's question. "
            "For follow-up questions, consider both the current context and the previous conversation. "
            "If you don't have enough information to answer a question, say so."
        )

        prompt = f"""Previous conversation:
{history_text}

Context:
{context_text}

Current question: {user_message}"""

        # Get response from GPT
        chat_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )

        answer = chat_response.choices[0].message.content

        # Store the interaction in memory
        conversation_memory[session_id].append({
            "user": user_message,
            "assistant": answer,
            "context": context_text
        })

        return jsonify({
            "success": True,
            "response": answer,
            "debug": {
                "contexts_found": len(contexts),
                "memory_size": len(conversation_memory[session_id])
            }
        })

    except Exception as e:
        logger.error(f"Chat error: {str(e)}", exc_info=True)
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Add a new endpoint to get conversation history
@app.route("/api/history", methods=["GET"])
def get_history():
    session_id = request.args.get("session_id", "default")
    if session_id in conversation_memory:
        return jsonify({
            "success": True,
            "history": list(conversation_memory[session_id])
        })
    return jsonify({
        "success": False,
        "error": "No history found"
    })

# Add endpoint to clear history
@app.route("/api/clear-history", methods=["POST"])
def clear_history():
    try:
        data = request.get_json()
        session_id = data.get("session_id", "default")
        if session_id in conversation_memory:
            conversation_memory[session_id].clear()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

def status_update(message):
    """Helper function to send SSE updates to frontend"""
    logger.info(message)
    return jsonify({"status": message})

@app.route("/api/end-session", methods=["POST"])
def end_session():
    try:
        data = request.get_json()
        session_id = data.get("session_id")
        persist = data.get("persist", False)

        if not persist:
            embedding_manager.delete_temporary_embeddings(session_id)
            status_update("Cleaned up temporary embeddings")

        return jsonify({"success": True})

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)