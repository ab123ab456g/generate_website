from flask import render_template, flash, redirect, request, url_for

from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/registor')
def registor():
	return render_template('registor.html')

@app.route('/user/<username>')
def user(username):
	return render_template('user.html')

@app.route('/edit')
def edit():
	return render_template('edit_profile.html')

@app.route('/500')
def error_500():
	return render_template('500.html')

@app.route('/404')
def error_404():
	return render_template('404.html')