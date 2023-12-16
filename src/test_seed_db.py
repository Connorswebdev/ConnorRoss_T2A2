import unittest
from init import db
from app import setup
from models.user import User
from blueprints.cli_bp import seed_db

# This python file is explicitly used to test the seeding is working as intended. To test that data is being seeded,

class DatabaseSeedingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = setup()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_seed_db(self):
        with self.app.app_context():
            seed_db()

        with self.app.app_context():

            # Testing that user is seeded correctly
            user_count = db.session.query(User).count()
            self.assertEqual(user_count, 3, "Expected 3 users after seeding")
\

if __name__ == '__main__':
    unittest.main()
