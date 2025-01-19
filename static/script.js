let sessionId = localStorage.getItem('sessionId') || 'default';
let messageHistory = [];

async function processUrl() {
    const button = document.querySelector('.process-btn');
    const originalText = button.innerHTML;
    
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
    button.disabled = true;
    
    const url = document.getElementById('urlInput').value;
    const isSitemap = document.getElementById('isSitemap').checked;
    const persistEmbeddings = document.getElementById('persistEmbeddings').checked;
    
    try {
        updateStatus('Processing URL...');
        const response = await fetch('/api/process-url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                url: url,
                is_sitemap: isSitemap,
                persist_embeddings: persistEmbeddings
            })
        });
        
        const data = await response.json();
        if (data.success) {
            updateStatus('Processing completed successfully');
        } else {
            updateStatus('Error: ' + data.error);
        }
    } catch (error) {
        updateStatus('Error: ' + error.message);
    }
    
    // Reset button after processing
    setTimeout(() => {
        button.innerHTML = originalText;
        button.disabled = false;
        
        // Optionally collapse the upload section after processing
        toggleUpload();
    }, 2000);
}

async function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value.trim();
    
    if (!message) return;
    
    // Add user message
    addMessageToChat('user', message);
    messageInput.value = '';
    
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                message: message,
                session_id: sessionId
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            addMessageToChat('assistant', data.response);
            
            // Store in message history
            messageHistory.push({
                user: message,
                assistant: data.response
            });
            
            // Keep only last 5 interactions
            if (messageHistory.length > 5) {
                messageHistory.shift();
            }
        } else {
            addMessageToChat('assistant', 'Error: ' + data.error);
        }
    } catch (error) {
        addMessageToChat('assistant', 'Error: Failed to send message. Please try again.');
    }
}

function addMessageToChat(role, content) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}-message`;
    
    if (role === 'assistant') {
        // Configure marked options
        marked.setOptions({
            breaks: true,
            gfm: true,
            headerIds: false,
            mangle: false
        });
        
        // Clean up content
        const cleanContent = content
            .replace(/\n\s*\n/g, '\n')
            .trim();
            
        messageDiv.innerHTML = marked.parse(cleanContent);
    } else {
        messageDiv.textContent = content;
    }
    
    // Add animation class
    messageDiv.classList.add('message-animation');
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    // Trigger animation
    setTimeout(() => {
        messageDiv.classList.add('show');
    }, 100);
}

async function endSession() {
    if (currentSessionId) {
        const persistEmbeddings = document.getElementById('persistEmbeddings').checked;
        await fetch('/api/end-session', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                session_id: currentSessionId,
                persist: persistEmbeddings
            })
        });
    }
}

function updateStatus(message) {
    document.getElementById('status').textContent = message;
}

// Add event listener for Enter key
document.getElementById('messageInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Add event listener for page unload
window.addEventListener('beforeunload', endSession);

function toggleUpload() {
    const uploadSection = document.getElementById('uploadSection');
    const toggleButton = document.querySelector('.upload-toggle');
    
    uploadSection.classList.toggle('expanded');
    toggleButton.classList.toggle('expanded');
}

function adjustChatMessages() {
    const chatMessages = document.getElementById('chat-messages');
    const uploadSection = document.getElementById('uploadSection');
    const isExpanded = uploadSection.classList.contains('expanded');
    
    chatMessages.style.height = isExpanded ? 'calc(100% - 300px)' : '100%';
}

// Add function to clear history
async function clearHistory() {
    try {
        await fetch('/api/clear-history', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ session_id: sessionId })
        });
        
        messageHistory = [];
        const chatMessages = document.getElementById('chat-messages');
        chatMessages.innerHTML = '';
        
        addMessageToChat('assistant', 'Conversation history has been cleared.');
    } catch (error) {
        console.error('Failed to clear history:', error);
    }
}