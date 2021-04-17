from flask_restful import Resource, reqparse
from models.credit import CreditModel
import pandas as pd

class Credit(Resource):

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
    parser.add_argument('risk',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, id):
        credit = CreditModel.find_by_id(id)
        if credit:
            return credit.json()
        return {'message': 'Data not found'}, 404

    def post(self):

        data = Credit.parser.parse_args()
        
        credit = CreditModel(**data)
        try:
            credit.save_to_db()
        except:
            return {'message': "An error occured while creating the credit"}, 500

        return credit.json(), 201

    def delete(self, id):
        credit = CreditModel.find_by_id(id)
        if credit:
            credit.delete_from_db()

        return {'message': 'Credit deleted'}

class CreditList(Resource):
    def get(self):
        return {'data': [credit.json() for credit in CreditModel.find_all()]}

class CreditImport(Resource):
    def get(self):
        df = pd.read_csv('dataset.csv')
        df = df.to_dict('records')

        for data in df:
            credit = CreditModel(**data)
            try:
                credit.save_to_db()
            except Exception as e:
                return {
                    'message': f"An error occured while creating the credit: {e}",
                    'error_data': f"{data}"
                }, 500

        return {'message': 'Dataset uploaded'}

