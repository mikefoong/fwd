from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    # return '<h1>Hello FLASK! </h1><p>Your Browser is {}</p>'.format(user_agent)
    return render_template('index.html', browser = user_agent, current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    return render_template('user.html', name = name, browser = user_agent, current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    user_agent = request.headers.get('User-Agent')
    return render_template('404.html', browser = user_agent, current_time=datetime.utcnow()), 404

@app.errorhandler(500)
def internal_server_error(e):
    user_agent = request.headers.get('User-Agent')
    return render_template('500.html', browser = user_agent, current_time=datetime.utcnow()), 500
