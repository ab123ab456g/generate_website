import unittest
from datetime import datetime, timedelta
from app import app, db
from app.models import *


class TestUserModel(unittest.TestCase):
	def setUp(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()


if __name__ == '__main__':
	unittest.main(verbosity=2)