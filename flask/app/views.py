from app import app
from flask import Flask, Response
from json import dumps


def getResponse():
    return ["one", 7, "three"]

@app.route('/')
def index():
    return Response(
            status = 200,
            mimetype = "application/json",
            content_type = "application/json",
            response = dumps(getResponse())
    )
