from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import emoji

app = Flask(__name__, static_url_path='/static')

# Load a pre-trained emotion detection model
emotion_classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-emotion")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data['text']

    # Use the emotion classifier to detect the emotion in the text
    results = emotion_classifier(text)

    # Extract the detected emotion from the results
    detected_emotion = results[0]['label']

    # Define a mapping from detected emotions to emojis
    emotion_to_emoji = {
        'anger': ':angry:',
        'disgust': ':nauseated_face:',
        'fear': ':fearful:',
        'joy': ':grinning:',
        'sadness': ':cry:',
        'surprise': ':astonished:',
    }

    # Get the emoji for the detected emotion (default to question mark if not found)
    emoji_code = emotion_to_emoji.get(detected_emotion, ':question:')

    # Use the emoji library to convert emoji codes to actual emojis
    emoji_icon = emoji.emojize(emoji_code, use_aliases=True)

    # Determine overall sentiment based on detected emotion
    sentiment = 'positive' if detected_emotion == 'joy' else 'negative' if detected_emotion in ['anger', 'disgust', 'fear', 'sadness'] else 'neutral'

    return jsonify({'sentiment': sentiment, 'emotion': detected_emotion, 'emoji': emoji_icon})

if __name__ == '__main__':
    app.run(debug=True)
