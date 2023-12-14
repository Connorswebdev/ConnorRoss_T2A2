import unittest
from init import db
from app import create_app
from models.user import User
from cli_bp import seed_db

class DatabaseSeedingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_seed_db(self):
        with self.app.app_context():
            seed_db()

        with self.app.app_context():
            # Check if the expected data is present in the database after seeding
            # Add your assertions here based on the expected data

            # Example:
            user_count = db.session.query(User).count()
            self.assertEqual(user_count, 3, "Expected 3 users after seeding")

            # Continue with similar assertions for other models

if __name__ == '__main__':
    unittest.main()
