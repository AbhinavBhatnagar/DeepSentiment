import requests
import json
import subprocess
import os

class DeepSentiment:
    def __init__(self):
        self.parameter = []
        self.text = ""
        self.sentiment = ""
        self.sentiment_score = 0
        self.proc = None

    def run_server(self):
        call_ = ['nohup','java', '-jar', str(os.getcwd()) +"/DeepSentiment/resources/deepsentiment.jar"]
        self.proc = subprocess.Popen(call_)

    def get_text(self, text):
        self.text = text
        return self.text

    def deepsentiment(self, text):
        self.parameter = [('text',text)]
        response = requests.get("http://127.0.0.1:9000/", params=self.parameter)
        jresponse = json.loads(response.text)
        return jresponse

    def get_sentiment(self, jresponse):
        self.sentiment = jresponse["sentiment"]
        return self.sentiment

    def get_sentiment_score(self, jresponse):
        self.sentiment_score = jresponse["sentimentscore"]
        return self.sentiment_score

    def stop_server(self):
        self.proc.terminate()

