#!/usr/bin/env python
from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
POSTGRES_USER=os.environ['POSTGRES_USER']
POSTGRES_PW=os.environ['POSTGRES_PW']
POSTGRES_HOST=os.environ['POSTGRES_HOST']
POSTGRES_DB=os.environ['POSTGRES_DB']

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}/{}'.format(POSTGRES_USER,POSTGRES_PW,POSTGRES_HOST,POSTGRES_DB)
db = SQLAlchemy(app)

# tables schema
class User(db.Model):
    __tablename__ = "users"
    name = db.Column(db.String(120), unique=True, primary_key=True)
    color = db.Column(db.String(120))
    animal = db.Column(db.String(3))

    def __init__(self, name, color, animal):
        self.name = name
        self.color = color
        self.animal = animal

@app.route('/')
def input_data():
    return render_template('input_data.html')

@app.route('/', methods=['POST'])
def input_data_post():
    name = request.form['name']
    color = request.form['color']
    animal = request.form['animal']

    #lookup for duplicate `Name`
    if not db.session.query(User).filter(User.name == name).count():
        db.session.add(User(name,color,animal))
        db.session.commit()
        return 'Success'
    return 'Duplicate name'

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=False, port=8000)
