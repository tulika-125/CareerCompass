from flask import Flask, request, jsonify, send_from_directory
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Flask app
app = Flask(__name__, static_folder='.', static_url_path='')

# Define the system prompt constraint for the AI
SYSTEM_PROMPT = """You are the "Career Compass AI", a friendly, knowledgeable career counselor built into the Career Compass website.
Your goal is to help students discover the best career path based on their interests.

When the user first says hello or asks for help, introduce yourself and ask 2-3 specific, engaging questions about:
1. Their favorite subjects in school.
2. Their hobbies or what they enjoy doing in their free time.
3. Their preferred working style.

Once they answer, recommend 1 or 2 specific careers.
CRITICALLY IMPORTANT: The website has 4 main streams (Science, Arts, Commerce, Medical).
When you recommend a career, encourage them to "Explore our dedicated pages by clicking the buttons on the main page" or mention the specific stream they should look into (e.g., "Check out the Science section for Engineering!").

Keep your responses concise, encouraging, and formatted with clear spacing. DO NOT write essays."""

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or 'messages' not in data:
        return jsonify({"error": "No messages provided"}), 400
        
    user_messages = data['messages']
    
    # Prepend the system prompt
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + user_messages
    
    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 400
        }
        
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        
        if response.status_code == 200:
            ai_response = response.json()['choices'][0]['message']['content']
            return jsonify({"response": ai_response})
        else:
            print("HTTP Status Error:", response.text)
            return jsonify({"error": "Error getting response from AI"}), 500
            
    except Exception as e:
        print("Exception Error communicating with API:", e)
        return jsonify({"error": "Failed to get response from AI. Please try again later."}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
