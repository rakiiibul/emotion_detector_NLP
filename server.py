"""
This module defines the Emotion Detector server using Flask.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection  import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")

def emotiondetector():
    """
    Endpoint for the Emotion Detector.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    dom = emotion_detector(text_to_analyze)
    if dom is None:
        return "Invalid text! Please try again!."
    dominated=max(dom,key=dom.get)
    result=f"For the given statement, the system response is {dom}."
    result+=f"The dominant emotion is {dominated}."
    return result
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
