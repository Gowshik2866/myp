import random
from transformers import pipeline
import matplotlib.pyplot as plt

user_data = {}

sentiment_analysis_pipeline = pipeline("sentiment-analysis")
emotion_detection_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
text_generation_pipeline = pipeline("text-generation", model="gpt2")

def store_user_response(session_id, key, value):
    if session_id not in user_data:
        user_data[session_id] = {'moods': [], 'concerns': [], 'emotions': [], 'rewards': 0, 'preferred_techniques': {}}
    user_data[session_id][key].append(value)

def assess_mood(user_input):
    try:
        sentiment = sentiment_analysis_pipeline(user_input)[0]['label'].lower()
        return "positive" if sentiment == "positive" else "negative" if sentiment == "negative" else "neutral"
    except:
        return "neutral"

def detect_emotion(user_input):
    try:
        return emotion_detection_pipeline(user_input)[0]['label'].lower()
    except:
        return "neutral"

def detect_crisis(user_input):
    crisis_keywords = ["suicide", "self-harm", "hopeless", "give up", "can't go on"]
    return any(word in user_input.lower() for word in crisis_keywords)

def handle_crisis():
    return "I'm really sorry you're feeling this way. Please reach out to a professional. Here is a crisis hotline: 1800-599-0019."

def reward_user(session_id):
    user_data[session_id]['rewards'] += 1
    return f"Congratulations! You've reached {user_data[session_id]['rewards']} wellness points! Keep up the great work!" if user_data[session_id]['rewards'] % 5 == 0 else ""

def suggest_grounding_techniques(session_id):
    preferences = user_data[session_id].get('preferred_techniques', {})
    if preferences:
        most_preferred = max(preferences, key=preferences.get)
        return f"It seems you prefer {most_preferred} exercises. Would you like to try that again?"
    
    grounding_suggestions = [
        "How about the '5-4-3-2-1' grounding technique? Focus on five things you can see, four you can touch, etc.",
        "Would you like to practice deep breathing with me?",
        "We can also try progressive muscle relaxation."
    ]
    return random.choice(grounding_suggestions)

def store_preference(session_id, technique):
    if technique not in user_data[session_id]['preferred_techniques']:
        user_data[session_id]['preferred_techniques'][technique] = 1
    else:
        user_data[session_id]['preferred_techniques'][technique] += 1

def generate_response(prompt):
    try:
        return text_generation_pipeline(prompt, max_length=50, num_return_sequences=1)[0]['generated_text'].strip()
    except:
        return "I'm sorry, something went wrong. Could you tell me more?"

def personalized_response(user_input, session_id):
    mood = assess_mood(user_input)
    emotion = detect_emotion(user_input)
    store_user_response(session_id, 'moods', mood)
    store_user_response(session_id, 'emotions', emotion)
    
    if mood == "positive":
        prompt = f"You're feeling {mood} with {emotion}. That's wonderful! What else has been making you feel good?"
    elif mood == "negative":
        prompt = f"It seems like you're feeling {mood} and experiencing {emotion}. I'm here to listen."
        prompt += f" {suggest_grounding_techniques(session_id)}"
        store_preference(session_id, "grounding")
    else:
        prompt = "It seems like you're feeling neutral. Would you like to share more?"
    
    return generate_response(prompt)

def start_chatbox_conversation(session_id, user_input):
    if detect_crisis(user_input):
        return handle_crisis()
    return personalized_response(user_input, session_id)

def plot_mood_chart(session_id):
    moods = user_data[session_id]['moods']
    mood_values = [1 if mood == "positive" else (-1 if mood == "negative" else 0) for mood in moods]
    plt.plot(mood_values, marker='o')
    plt.title('Your Mood Over Time')
    plt.xlabel('Session Interactions')
    plt.ylabel('Mood (1=Positive, 0=Neutral, -1=Negative)')
    plt.show()