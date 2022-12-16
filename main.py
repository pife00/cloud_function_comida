from pollo_alimento import toSend
from flask import  jsonify
from flask_cors import cross_origin
from group_sms import groupSms

import functions_framework

@cross_origin()
@functions_framework.http
def comida_http(request):
    return jsonify(toSend)

@cross_origin()
@functions_framework.http
def sms_debts_resumen(request):
    payload = request.get_json(force=True)
    debts = groupSms(payload)
    return jsonify(debts)
    