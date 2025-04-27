from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    # Use VADER for primary sentiment analysis
    vader_scores = vader_analyzer.polarity_scores(text)
    compound_score = vader_scores['compound']

    if compound_score >= 0.05:
        mood = 'positive'
    elif compound_score <= -0.05:
        mood = 'negative'
    else:
        mood = 'neutral'

    return mood

def suggest_activities(mood):
    if mood == 'positive':
        return ['Go for a walk in the park 🌳', 'Call a friend and celebrate 🎉', 'Start a new creative project 🎨']
    elif mood == 'negative':
        return ['Listen to calming music 🎶', 'Practice deep breathing 🧘', 'Write down your thoughts ✍️']
    else:
        return ['Read a book 📚', 'Do a light workout 🏃‍♂️', 'Plan your next day 🗓️']
