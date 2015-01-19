from flask import Flask, render_template, request, jsonify, flash, redirect,session,url_for,abort
import os			#used
import requests
from flask.ext.wtf import Form #used
from wtforms import *			
from wtforms.validators import Required 
from flask_wtf.csrf import CsrfProtect #important for any database stuff
from flask.ext.mail import Mail, Message
from os import getenv 

def debug(): # use this to trigger the flask debugger
    assert current_app.debug == False

def pdb():
	if app.debug:
		import pdb
		pdb.set_trace()


app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)

csrf = CsrfProtect(app)



@app.route("/",methods=['GET','POST'])
def main():
	if request.method == 'GET':
	    return render_template('main.html')
	else:
		fromemail = request.form['fromemail']
		message = request.form['message']
		name = request.form['name']
		subject ="%s has contacted you"%name
		msg = Message(subject = subject, sender ='flasktemplatedemoacc@google.com', recipients = ['flasktemplatedemoacc@google.com']) #you need to change the sender and recipients
		msg.html = render_template('contacted.html', fromemail = fromemail, name=name, message=message)
		with app.app_context():
			mail.send(msg)
		return render_template('main.html')

@app.route("/blog",methods=['GET','POST'])
def blog():
	if request.method == 'GET':
	    return render_template('blog.html')
	else:
		fromemail = request.form['fromemail']
		message = request.form['message']
		name = request.form['name']
		subject ="%s has contacted you"%name
		msg = Message(subject = subject, sender ='flasktemplatedemoacc@google.com', recipients = ['flasktemplatedemoacc@google.com']) #you need to change the sender and recipients
		msg.html = render_template('contacted.html', fromemail = fromemail, name=name, message=message)
		with app.app_context():
			mail.send(msg)
		return render_template('blog.html')


if __name__ == "__main__":
	app.debug = getenv('DEBUG', True)
	app.run(host='0.0.0.0', port=8000)
