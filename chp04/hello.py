from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

moment = Moment(app)
app.config['SECRET_KEY'] = 'I am Human'
app.config['DEBUG'] = True

class NameForm(FlaskForm):
    name = StringField('Tell me your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    user_agent = request.headers.get('User-Agent')
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', browser = user_agent, current_time = datetime.utcnow(), form = form, name = session.get('name'))

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
