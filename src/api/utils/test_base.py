import unittest2 as unittest
from src.main import create_app
from api.utils.database import db
from api.config.config import TestingConfig
import tempfile

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app(TestingConfig)
        with app.app_context():
            db.create_all()
        app.app_context().push()
        self.app = app.test_client()

    def tearDown(self):
        db.session.close_all()
        db.drop_all()

        
        

