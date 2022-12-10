from pollo_alimento import toSend
from flask import escape,jsonify
import functions_framework

@functions_framework.http
def comida_http(request): 
    return jsonify(toSend)