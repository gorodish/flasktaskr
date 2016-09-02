# db_create.py

from views import db
from models import Task
from datetime import date

# create the database and the db table
db.create_all()

#insert data
db.session.add(Task("Do item 1", date(2016, 9, 1), 10, 1))
db.session.add(Task("Do item 2", date(2016, 9, 1), 10, 1))
db.session.commit()