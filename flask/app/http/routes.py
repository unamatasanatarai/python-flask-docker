from app.http import app
from flask import Flask, Response, request
from html import escape
from json import dumps
from os.path import dirname
from app.view import render

def getLinks():
    return [
        "/json",
        "/text",
        "/text/YOUR_TEXT",
        "/text/YOUR_TEXT/and?then=YOUR_QUERY_TEXT",
    ]

views = dirname(dirname(__file__))+'/resources/views'

@app.route('/')
def index():
    return render('index.html', directory=views, links=getLinks())

@app.route('/json')
def json():
    return Response(
        status = 200,
        mimetype = "application/json",
        content_type = "application/json",
        response = dumps(getLinks())
    )

@app.route('/text')
def text():
    return "pure simple text"

@app.route('/text/<input>')
def textinput(input = None):
    input = escape(input)
    return f'You said: {input}'


@app.route('/text/<input>/and')
def textinputand(input = None):
    input = escape(input)
    q = escape(request.args.get('then', default="nothing"))
    return f'You said: {input} and {q}'