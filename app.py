from flask import Flask, render_template, request, jsonify
from config import Config
from dotenv import load_dotenv
import os

# Import sentiment functions from sentiment_utils
from sentiment_utils import analyze_sentiment, suggest_activities

load_dotenv()  # Load environment variables

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form.get('user_text')
        mood = analyze_sentiment(user_text)
        activities = suggest_activities(mood)
        return render_template('index.html', 
                            mood=mood, 
                            activities=activities,
                            user_text=user_text)
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.get_json()
    mood = analyze_sentiment(data['text'])
    return jsonify({
        'mood': mood,
        'activities': suggest_activities(mood)
    })

if __name__ == '__main__':
    app.run(debug=True)
