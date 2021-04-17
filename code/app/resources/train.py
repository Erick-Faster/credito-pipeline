from flask import Flask
from flask_restful import Resource
import json
import requests
from instances import config

class Train(Resource):

    def get(self):
        headers = {"Content-Type": "application/json"}
        response_json = requests.get(config.URL_TRAINING, headers=headers)
        response = json.loads(response_json.content)
        return response