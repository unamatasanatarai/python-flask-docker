from app import app
from flask import Flask, Response, request, render_template
from html import escape
from json import dumps
from os.path import dirname

def getLinks():
    return [
        "/json",
        "/text",
        "/text/YOUR_TEXT",
        "/text/YOUR_TEXT/and?then=YOUR_QUERY_TEXT",
    ]

@app.route('/')
def index():
    return render_template('home/index.html', links=getLinks())

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
    return render_template('home/text.html')

@app.route('/text/<input>')
def textinput(input = None):
    input = escape(input)
    return render_template('home/textinput.html', input=input)


@app.route('/text/<input>/and')
def textinputand(input = None):
    input = escape(input)
    q = escape(request.args.get('then', default="nothing"))
    return render_template('home/textinputand.html', input=input, then=q)
