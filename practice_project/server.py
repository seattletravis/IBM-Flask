from flask import Flask, render_template, request
from sentiment_analysis import sentiment_analyzer
import json
app = Flask(__name__)


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO
    return 
    # return sentiment_analyzer(text_to_analyse)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO
    result = sentiment_analyzer("I love this new tech.")
    # return render_template(result)

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO
    app.run()

print(sentiment_analyzer("I love this new tech."))