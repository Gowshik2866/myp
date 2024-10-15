from flask import Flask, render_template, request, jsonify
from chatbot import get_chatbot_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    bot_response = get_chatbot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '_main_':
    app.run(debug=True)