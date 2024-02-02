"""import json, requests libs"""
import json
import requests
def emotion_detector(text_to_analyse):
    """For this project, you'll use the Emotion Predict function of the Watson NLP Library."""
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input, headers=header)
    formatted_response = json.loads(response.text)
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
    contenders = {'anger':anger_score,'disgust':disgust_score,'fear':fear_score,'joy':joy_score,'sadness':sadness_score}
    dominant_emotion = max(contenders, key=contenders.get)
    
    return {'dom emotion': dominant_emotion}
    # emotions = {
    #     'anger': anger_score,
    #     'disgust': disgust_score,
    #     'fear': fear_score,
    #     'joy': joy_score,
    #     'sadness': sadness_score,
    #     'dominant_emotion': dominant_emotion
    # }
    # return anger_score