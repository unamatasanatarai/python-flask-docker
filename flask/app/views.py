from app import app
from flask import Flask, Response, request
from json import dumps
from html import escape
from jinja2 import Template, Environment, FileSystemLoader
from os import path

def getLinks():
    return [
    	"/json",
    	"/text",
    	"/text/YOUR_TEXT",
    	"/text/YOUR_TEXT/and?then=YOUR_QUERY_TEXT",
    ]

@app.route('/')
def index():
	file_loader = FileSystemLoader(path.dirname(__file__))
	env = Environment(loader=file_loader)
	template = env.get_template('index.html')
	return template.render(links=getLinks())

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