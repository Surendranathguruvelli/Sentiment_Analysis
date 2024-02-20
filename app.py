from flask import Flask, render_template, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__, static_url_path='/static')

# Create a sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():                                                                                                                                                                                                                                                                                                                                                                              
    data = request.get_json()
    text = data['text']

    # Perform sentiment analysis using NLTK's VADER
    sentiment_scores = analyzer.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Add logic to determine emotion and emoji based on sentiment_scores if needed
    # For example:
    emotion = 'Happy' if sentiment == 'Positive' else 'Sad' if sentiment == 'Negative' else 'Neutral'
    emoji = '😄' if sentiment == 'Positive' else '😢' if sentiment == 'Negative' else '😐'

    return jsonify({'sentiment': sentiment, 'emotion': emotion, 'emoji': emoji})

if __name__ == '__main__':
    app.run(debug=True)
