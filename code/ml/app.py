from flask import Flask
from flask_restful import Api
from train_model import Train
from instances import config

app = Flask(__name__)
app.secret_key = 'fast2'
api = Api(app)

api.add_resource(Train, '/pipeline')

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)