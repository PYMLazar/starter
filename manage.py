from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from models import db
print ("manage py 1")
migrate = Migrate(app, db)
manager = Manager(app)
print ("manage py 2")
manager.add_command('db', MigrateCommand)
print ("manage py 3")

if __name__ == '__main__':
    print ("manage py 4")
    manager.run()