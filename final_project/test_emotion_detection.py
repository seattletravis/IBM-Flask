from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_sentiment_analyser(self):
        result_1 = emotion_detector("I am glad this is happening")
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        result_1 = emotion_detector("I am really mad about this")
        self.assertEqual(result_1['dominant_emotion'], 'anger')
        result_1 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_1['dominant_emotion'], 'disgust')
        result_1 = emotion_detector("I am so sad about this")
        self.assertEqual(result_1['dominant_emotion'], 'sadness')
        result_1 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_1['dominant_emotion'], 'fear')

        
unittest.main()