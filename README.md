# Flask Web Design
## Codebook

Codebook for Flask Web Design - 2nd Edition.

Setup
-----

1. Install python 3.6
2. Install pip3
3. Create environment variables
* define FLASK_APP (hello.py in this case)
> export FLASK_APP=hello.py

* set FLASK_DEBUG to true
> export FLASK_DEBUG=1



Dependencies
------------

1. install Flask
> $ pip3 install flask

2. Install flask-bootstrap
> $ pip3 install flask-bootstrap

3. Install flask-moment
> $ pip3 install flask-moment

4. Install flask-wtf
> $ pip install flask-wtf

5. Install flask-sqlalchemy
> $ pip3 install flask-sqlalchemy

6. Install flask-migrate
> $ pip3 install flask-migrate

7. Install flask-mail
> $ pip3 install flask-mail

### Update: 201830Ma+65
-----------------------

Chapter 5 - Databases
Database Framework using Flask-SQLAlchemy. Integration with flask.

1. Started on Chapter 5
2. Created ch05 dir
3. Install Flask-SQLAlchemy
> $ pip install flask-sqlalchemy

4. Created a SQLite Database
5. Created 2 tables (users, roles)
6. Added (admin, moderator and user roles)
7. Created dummy users (john, susan, dave, mikefoong)
8. Amended the hello.py to accept Known users from the Database
9. Register new users if they are not known and add them to the database
10. Create a shell context processor to ensure that the context are always set when using Flask Shell
11. Installed Flask-Migrate
12. Flask-Migrate allows database schemas to be tracked
13. Flask-Migrate is a lightweight Albemic Wrapper that integrates with the Flask command
14. Albemic is a migration framework for SQLAlchemy
> $ pip install flask-migrate

15. Create a db migration directory

### Update: 201801Ap+65
-----------------------

Chapter 6 - Email
Using an external email or mail transport agent (SMTP)

1. Code for Chapter 6 is in ch06 dir
2. Install flask-mail
3. Added Mail server configuration in app.config
4. mail = Mail(app) app context needs to be after config
5. Integrating flask_mail in the app
6. Set environment variables to ensure that it is not captured in the code
* MAIL_USERNAME
* MAIL_PASSWORD
* FLASKY_ADMIN
7. Create Threads to enable async email sending
