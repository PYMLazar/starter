import os
from sqlalchemy import Column, String, create_engine, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
print(1)
def setup_db(app, database_path=database_path):
    print(2)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    print(3)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    print(3)
    db.app = app
    print(4)
    db.init_app(app)
    print(5)
    db.create_all()


'''
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}