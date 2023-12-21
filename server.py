'''
The main function of this server.py is to handle
the requests of the frontend and uses
proper function to generate desired output and
serve the results back to the frontend and also to
render the correct templates at correct place.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route("/emotionDetector")
def send_emotion_detection():
    '''
    This function takes the text given by the user
    and which is stored in the variable
    named 'textToAnalze' by the javascript. It then sends
    that text to the emotion_detector function
    for processing and then receives the response from the
     function and returns the desired output format.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please Try Again"
    return f"For the given statement, the system response is 'anger': {response['anger']}, " \
           f"disgust: {response['disgust']}, 'fear': {response['fear']}, "\
           f" joy : {response['joy']}, " \
           f"and 'sadness': {response['sadness']}. The dominant emotion is"\
           f" {response['dominant_emotion']}", 200

@app.route("/")
def index_page():
    '''
    This function is used to render the
     correct homepage of the website when
      the website it first opened.
    '''
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
