"""Module imports."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """Description of function"""
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']
    if dominant is None:
        return "Could not process your request!, Please Try again."
    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, \
        'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. The dominant emotion is {dominant}."

@app.route("/")
def render_index_page():
    """Description of function"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)