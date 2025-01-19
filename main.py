from openai import OpenAI
from supabase import create_client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set API keys and URLs
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)

class EmbeddingManager:
    def __init__(self):
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.session_id = None

    def create_session(self):
        """Create a new session ID for temporary embeddings"""
        import uuid
        self.session_id = str(uuid.uuid4())
        return self.session_id

    def store_embeddings_in_supabase(self, embeddings, is_temporary=True):
        """Store embeddings with session tracking"""
        for item in embeddings:
            data, count = self.supabase.table("embeddings").insert({
                "text": item["text"],
                "embedding": item["embedding"],
                "session_id": self.session_id if is_temporary else None,
                "is_temporary": is_temporary
            }).execute()

    def delete_temporary_embeddings(self, session_id):
        """Delete temporary embeddings for a session"""
        self.supabase.table("embeddings").delete().eq("session_id", session_id).execute()

# 1. Preprocess the Markdown File
def preprocess_markdown(file_path, chunk_size=500):
    """
    Preprocess the Markdown file into smaller chunks.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
    return chunks

# 2. Generate Embeddings with Batching
def generate_embeddings_with_batching(chunks, batch_size=10):
    """
    Generate embeddings for text chunks in batches.
    """
    embeddings = []
    for i in range(0, len(chunks), batch_size):
        # Create a batch of chunks
        batch = chunks[i:i + batch_size]
        
        # Generate embeddings for the batch
        response = openai_client.embeddings.create(
            input=batch,
            model="text-embedding-3-small"
        )
        
        # Store embeddings from the batch
        for text, embedding in zip(batch, response.data):
            embeddings.append({
                "text": text,
                "embedding": embedding.embedding
            })
    return embeddings

if __name__ == "__main__":
    # File path for the Markdown file
    file_path = r"C:\Users\harsh\Downloads\MS projects\Deepgram\RAG\scraped_content.md"

    # Step 1: Preprocess Markdown File
    print("Preprocessing Markdown file...")
    chunks = preprocess_markdown(file_path)
    print(f"Total Chunks: {len(chunks)}")

    # Step 2: Generate Embeddings
    print("Generating embeddings for chunks...")
    embeddings = generate_embeddings_with_batching(chunks, batch_size=10)
    print(f"Generated {len(embeddings)} embeddings.")

    # Step 3: Store Embeddings in Supabase
    print("Storing embeddings in Supabase...")
    embedding_manager = EmbeddingManager()
    embedding_manager.store_embeddings_in_supabase(embeddings)
    print("Embeddings stored successfully.")
