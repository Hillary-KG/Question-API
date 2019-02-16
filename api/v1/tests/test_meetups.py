
import unittest
from flask import jsonify
from ... import create_app
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

    def test_get_one_meetup(self):
        '''testing fetching  of one meetup record'''
        res_post = self.client.post('/api/v1/meetups/',data=json.dumps(self.meetup), content_type="application/json")
        meetup_id = json.loads(res_post.data)['data']['id']
        res_get = self.client.get('/api/v1/meetups/{}'.format(meetup_id), data=json.dumps(self.meetup),content_type='application/json')
        self.assertEqual(res_get.status_code, 200)
        self.assertIn('Python', json.loads(res_get.data)['data']['topic'])


if __name__ == "__main__":
    unittest.main()
