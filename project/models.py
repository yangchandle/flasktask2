# project/models.py


from views import db

import datetime

class Task(db.Model):
  
    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integger, db.ForeignKey('users.id'))

    def __init__(self, name, due_date, prority, status):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.status =status
        self.user_id = user_id

    def __repr__(self):
        return '<name {0}>'.format(self.name)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Colume(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=True, nullable=False)
    password = db.Column(db.string, nullable=False)
    tasks = db.relationship('Task', backref='poster')

    def __init__(self, name= None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User {0}>'.form(self.name)
