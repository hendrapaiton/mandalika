import json
import unittest

from app import app
from models.db import db


class MyTestCase(unittest.TestCase):

    # Auto Setup before Unit Test Running
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    # Unit Test for Successful Login
    def test_successful_login(self):
        username = "admin@nj.net"
        password = "enje123"
        payload = json.dumps({
            "username": username,
            "password": password
        })
        response = self.app.post('/api/v1/login', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

    # Auto Setup after Unit Test Running
    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)


if __name__ == '__main__':
    unittest.main()
