import requests
import json
import pickle
from datetime import datetime
import pandas as pd
from instances import config
import boto3
from botocore.exceptions import NoCredentialsError

def extract_data(url):
    
    headers = {"Content-Type": "application/json"}
    response_json = requests.get(url, headers=headers)
    data = json.loads(response_json.content)
    df = pd.json_normalize(data['data'])
    df.drop(config.DROP_FEATURES, axis=1, inplace=True)

    print(f'Data extract successful! Num of elements: {df.shape[0]}')
    return df

def download_from_aws(down_file, s3_file):

    s3 = boto3.client('s3', aws_access_key_id=config.ACCESS_KEY,
                      aws_secret_access_key=config.SECRET_KEY)
    try:
        s3.download_file(bucket, config.BUCKET, down_file)
        print("Download Successful")
        return True
    except FileNotFoundError:
        print ("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not avaliable")
        return False
    

def upload_to_aws(local_file, s3_file):
    
    s3 = boto3.client('s3', aws_access_key_id=config.ACCESS_KEY,
                      aws_secret_access_key=config.SECRET_KEY)
    
    try:
        s3.upload_file(local_file, config.BUCKET, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print ("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not avaliable")
        return False

def load_pickle(filename):
    infile = open(filename,'rb')
    objeto = pickle.load(infile)
    infile.close()
    return objeto

def save_pickle(filepath, objeto, use_date=False):
    if use_date:
        date = datetime.now().strftime("-%Y-%m-%dT%H-%M-%S-%f")
        filepath = f'{filepath}{date}'
    outfile = open(f'{filepath}.pkl','wb')
    pickle.dump(objeto,outfile)
    outfile.close()