from flask_restful import Resource, reqparse
import pandas as pd
from instances import config
import json
import requests

class Predict(Resource):

    parser = reqparse.RequestParser() #Condicoes de entrada
    parser.add_argument('age',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('sex',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('job',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('housing',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('saving_accounts',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('checking_account',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('credit_amount',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('duration',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('purpose',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):

        data = Predict.parser.parse_args()
        headers = {"Content-Type": "application/json"}
        json_data = json.dumps(data).encode('utf8')
        response_json = requests.post(config.URL_TRAINING, data = json_data, headers = headers)
        response = json.loads(response_json.content)
        output = response['output']

        return {'output': output}





        


