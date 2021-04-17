import os

#Database conection

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']

'''
user = 'test'
password = 'password'
host = 'postgres'
database = 'example'
port = 5432
'''
DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

#App

HOST = '0.0.0.0'
PORT = 5000
DEBUG = False

#URL

URL_TRAINING = 'http://ml:6000/pipeline'