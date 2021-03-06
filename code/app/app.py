from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask import jsonify
from db import db
from instances import config
from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from resources.train import Train
from resources.credit import Credit, CreditList, CreditImport
from resources.predict import Predict
from datetime import timedelta
from blacklist import BLACKLIST

app = Flask(__name__)
app.secret_key = 'fast' # app.config['JWT_SECRET_KEY']
api = Api(app)

#app.config['JWT_AUTH_URL_RULE'] = '/login'
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
#app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI #Soh mudando essa linha posso usar MySQL, SQL, etc
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app) #Linka JWT ao app -> n cria /auth

@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1: #hardcode
        return {'is_admin': True}
    return {'is_admin': False}

'''
@jwt.token_in_blacklist_loader
def check_if_token_is_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST #posso usar decrypted_token['identity'] para banir um usuario


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description': 'The token has expired',
        'error': 'token_expired'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'description': 'Signature verification failed ',
        'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'description': 'Request does not contain an access token',
        'error': 'authorization_required'
    }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        'description': 'The token is not fresh',
        'error': 'fresh_token_required'
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'description': 'The token has been revoked',
        'error': 'token_revoked'
    }), 401
'''

'''
@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify({
        'access_token': access_token.decode('utf-8'),
        'user_id': identity.id
    })

@jwt.jwt_error_handler
def customized_error_handler(error):
    return jsonify({
        'message': error.description,
        'code': error.status_code
    }), error.status_code
'''

api.add_resource(CreditList, '/credits')
api.add_resource(Credit, '/credit')
api.add_resource(CreditImport, '/import')
api.add_resource(Train, '/train')
api.add_resource(Predict, '/predict')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(TokenRefresh, '/refresh')

if __name__ == '__main__': #evita que, ao importar app, nao execute novamente,
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG) #debug mostra msgs de erro