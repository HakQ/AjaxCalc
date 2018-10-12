from app import app
from flask import render_template, jsonify, request, redirect, url_for
import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
	try:
	    left = float(request.form['num1'])
	    right = float(request.form['num2'])
	    result = left+right
	    return jsonify({
	        'result': result
	    })
	except Exception:
	    return jsonify({
	        'result': "ERROR!"
	    })

@app.route('/subtract', methods=['POST'])
def subtract():
	try:
	    left = float(request.form['num1'])
	    right = float(request.form['num2'])
	    result = left-right
	    return jsonify({
	        'result': result
	    })
	except Exception:
	    return jsonify({
	        'result': "ERROR!"
	    })


@app.route('/multiply', methods=['POST'])
def multiply():
	try:
	    left = float(request.form['num1'])
	    right = float(request.form['num2'])
	    result = left*right
	    return jsonify({
	        'result': result
	    })
	except Exception:
	    return jsonify({
	        'result': "ERROR!"
	    })

@app.route('/divide', methods=['POST'])
def divide():
	try:
	    left = float(request.form['num1'])
	    right = float(request.form['num2'])
	    result = left/right
	    return jsonify({
	        'result': result
	    })
	except Exception:
	    return jsonify({
	        'result': "ERROR!"
	 })
