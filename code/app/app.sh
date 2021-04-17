#!/bin/sh

pip install bottle==0.12.13 psycopg2==2.7.3.2 redis==2.10.5
pip install flask
pip install pandas
pip install flask-sqlalchemy
pip install flask-jwt-extended
pip install flask-restful
pip install requests

python -u app.py