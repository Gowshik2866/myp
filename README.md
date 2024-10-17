Mindbot - Mental Health Support Assistant

Project Overview

Mindbot is a Flask-based web application designed to provide mental health support through a chatbot interface. The bot analyzes user inputs to assess mood, detect emotions, and offer personalized responses. It also stores user sessions in a SQLite database for tracking wellness over time.

Prerequisites

Before running this project, make sure the following software is installed:

Python 3.8 or higher

pip (Python package manager)

Flask

Hugging Face's Transformers library


Installation Instructions

1. Clone the Repository:

git clone https://github.com/Gowshik2866/myp.git
cd myp


2. Install Dependencies: Install all required Python packages:

pip install -r requirements.txt

If requirements.txt is missing, manually install the key dependencies:

pip install Flask transformers matplotlib sqlite3


3. Set Up the Database: The project uses SQLite for session storage. To create the database and necessary tables, run:

python chatbot.py

This will generate a therapybot.db file in the project directory.



Running the Application

1. Start the Flask Web Server: Run the following command to start the server:

python app.py

Flask will launch a development server at http://127.0.0.1:5000/.


2. Access the Application: Open a browser and go to http://127.0.0.1:5000/. You will be presented with the chat interface for interacting with Mindbot.


3. Interacting with Mindbot:

Type your message in the input field and click "Send".

Mindbot will respond based on its mood and emotion detection capabilities, and suggest techniques for grounding or provide further support.




Key Features

Mood & Emotion Detection: Mindbot uses sentiment analysis and emotion detection models from the Hugging Face Transformers library to understand the user's emotional state.

Crisis Detection: If keywords related to a mental health crisis (e.g., "suicide", "self-harm") are detected, the bot provides a crisis hotline.

Session Storage: User conversations and data are stored in an SQLite database, enabling the tracking of wellness over time.

Grounding Techniques: The bot suggests grounding exercises like deep breathing or progressive muscle relaxation, based on user preferences.


Project Structure

myp/
│
├── app.py                    # Flask application file (runs the server)
├── chatbot.py                # Chatbot logic (mood/emotion detection, session management)
├── templates/
│   └── chat.html             # HTML template for the chat interface
├── static/
│   └── script.js             # JavaScript for handling the frontend interaction
├── therapybot.db             # SQLite database for session data
├── requirements.txt          # Python dependencies

Usage Example

Send a message like "I feel anxious."

Mindbot will assess your mood and provide personalized responses, offering suggestions or techniques for coping.


Contributing

1. Fork this repository.


2. Create a new branch for your feature or bug fix.


3. Open a pull request when ready.
