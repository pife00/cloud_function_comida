from pollo_alimento import toSend
from flask import escape, jsonify
from flask_cors import cross_origin

import functions_framework

@cross_origin()
@functions_framework.http
def comida_http(request):
    return jsonify(toSend)
