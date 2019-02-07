
import unittest
from flask import jsonify
from api import create_app
import json

class TestMeetups(unittest.TestCase):
    def setUp(self):
        #creating app instance
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.meetup = {
                            "id":2,
                            "happening_on": "1/2/2019",
                            "created_on":"12/12/2018",
                            "location": "iHub",
                            "tags": [],
                            "topic": "Python Machine Leaning",
                            "images":[]
                        }

    def test_create_meetup(self):
        '''testing creation of a meetup record'''
        res = self.client.post('/api/v1/meetups/',data=json.dumps(self.meetup), content_type="application/json")
        res_data = json.loads(res.data)
        self.assertIn('Python',res_data['data']['topic'])
        self.assertEqual(res.status_code, 201)


if __name__ == "__main__":
    unittest.main()
