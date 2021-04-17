# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:04:22 2020

@author: erick
"""

import gradio as gr
import requests
import json

def predict_data(age, sex, job, housing, saving_accounts, checking_account, credit_amount, duration, purpose):
    
    data = {
        'age': age,
        'sex': sex,
        'job': job,
        'housing': housing,
        'saving_accounts': saving_accounts,
        'checking_account': checking_account,
        'credit_amount': credit_amount,
        'duration': duration,
        'purpose': purpose,
    }
    
    url = 'http://api:5000/predict'
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(data).encode('utf8')
    response_json = requests.post(url, data = json_data, headers = headers)
    response = json.loads(response_json.content)
    output = response['output']    
    
    return output

iface = gr.Interface(
    fn=predict_data, 
    inputs=[
        gr.inputs.Number(default=40, label='Age'),
        gr.inputs.Dropdown(['male', 'female'], label='sex'),
        gr.inputs.Radio([0,1,2,3], label='job'),        
        gr.inputs.Radio(['own', 'rent', 'free'], label='housing'),
        gr.inputs.Dropdown(['little', 'moderate', 'rich', 'quite rich'], label='saving_accounts'),
        gr.inputs.Dropdown(['little', 'moderate', 'rich'], label='checking_account'),        
        gr.inputs.Slider(minimum=0, maximum=10000, step=100, label='credit_amount'),
        gr.inputs.Slider(minimum=0, maximum=100, step=1, label='duration'),
        gr.inputs.Dropdown(['radio/TV', 'education', 'furniture/equipment', 'car', 'business'], label='purpose')       
    ],
    outputs=["text"],
    server_name="0.0.0.0")
if __name__ == '__main__':
    iface.launch()