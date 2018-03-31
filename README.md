# Flask Web Design
## Codebook

Codebook for Flask Web Design - 2nd Edition.

### Update: 201830Ma+65
=======================

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
16.   
