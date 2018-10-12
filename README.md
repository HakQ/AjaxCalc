Author: Qiuqun Wang

Project Purpose: A simple calculator with four basic arithmetic 

Language: Python, Flask, Javascript, HTML
OS: the program is coded in tested on Ubuntu 16.04 LTS

This program is a simple calculator that take two values and an operation
to perform on the two values. There are four routes that depending on the operation
the program will be route to. This is a pretty simple program with learning in mind.

To run the program:
1. clone the repository: git clone https://github.com/HakQ/AjaxCalc 
2. Go into the directory that you have just cloned
3. activate virtual environment: source venv/bin/activate. You may need to download
   virtualenv if you don't already have it
4. type: export FLASK_APP=calc.py. Also run export FLASK_ENV=development if you want to be in debug mode
5. type: flask run
6. A link will be provided after the previous step, click on the link and you 
   will be able to use the program.

How to use the program:
This is a pretty simple program to use. Provide two number and the
operation you want to perform on it and the program will do the calculation for you

Useful Links:
http://flask.pocoo.org/docs/1.0/tutorial/
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
https://www.tutorialspoint.com/flask/
https://github.com/pallets/flask/blob/master/.gitignore
