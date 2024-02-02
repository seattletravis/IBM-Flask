from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyser(self):
        result_1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        result_1 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(result_1['label'], 'SENT_NEGATIVE')
        result_1 = sentiment_analyzer("I an neutral on Python")
        self.assertEqual(result_1['label'], 'SENT_NEUTRAL')
        
        
unittest.main()