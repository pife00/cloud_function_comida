from flask import Flask,request,jsonify
import pandas as pd
from group_sms import groupSms

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def hello_world():
    if request.method == 'POST':
        
        payload = request.get_json(force=True)
        debts = groupSms(payload)
       # print(request.json)  # json (if content-type of application/json is sent with the request)
       # print(request.get_json(force=True))  # json (if content-type of application/json is not sent)
        return jsonify(debts)

if __name__ == '__main__':
    app.run(debug=True)