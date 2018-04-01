import os

from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_mail import Message
from threading import Thread

# Application definition are located here
app = Flask(__name__)
bootstrap = Bootstrap(app)
from flask_mail import Message
basedir = os.path.abspath(os.path.dirname(__file__))
moment = Moment(app)

# App Config has to be after app is defined
app.config['SECRET_KEY'] = 'I am Human'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <noreply@flaskyrawfactor.net>'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

# db definitions have to be after App Config with the database configuratins and options
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

# Blocking sync email sending
#def send_email(to, subject, template, **kwargs):
#    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender = app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#    msg.body = render_template(template + '.txt', **kwargs)
#    msg.html = render_template(template + '.html', **kwargs)
#    mail.send(msg)

# Threaded async email for better email management
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args = [app, msg])
    thr.start()
    return thr

@app.shell_context_processor
def make_shell_context():
    users = User.query.all()
    return dict(db=db, User=User, Role=Role)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_agent = request.headers.get('User-Agent')
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', browser = user_agent, current_time = datetime.utcnow(), form = form, name = session.get('name'), known = session.get('known', False))

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
