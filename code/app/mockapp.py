from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask import jsonify
from resources.train import Train

app = Flask(__name__)
app.secret_key = 'fast' # app.config['JWT_SECRET_KEY']
api = Api(app)

api.add_resource(Train, '/train')


if __name__ == '__main__': #evita que, ao importar app, nao execute novamente,

    app.run(host='0.0.0.0', port=5000, debug=False) #debug mostra msgs de erro