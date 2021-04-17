from flask_restful import Resource, reqparse
from processors.data_management import extract_data, upload_to_aws, save_pickle
from sklearn.model_selection import train_test_split
from pipeline import model
from instances import config
import pandas as pd
from processors.data_management import load_pickle

class Train(Resource):

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

    def get(self):

        df = extract_data(config.URL_DATA)

        X_train, X_test, y_train, y_test = train_test_split(df.drop(['risk'], axis=1), 
                                                    df['risk'], 
                                                    test_size=0.2, 
                                                    random_state=42)

        model.fit(X_train, y_train)

        train_score = model.score(X_train, y_train)

        save_pickle('trained_models/model', model)

        return {'train_score': train_score}

    def post(self):

        data = Train.parser.parse_args()

        df = pd.DataFrame.from_dict(data, orient ='index')
        df = pd.DataFrame(columns = df.index, data = (df.values).reshape(1,-1))

        model = load_pickle('trained_models/model.pkl')

        output = model.predict(df)

        return {'output': output[0]}
