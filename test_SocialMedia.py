import unittest
import json
from Que3 import app
class TestSocialMedia(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
    
    def test_postPosts(self):
        new_post = {'id': 1,' username': "alx", 'caption': "Sunny day!"}

        res = self.app.post('/post', json=new_post)
        data =  json.loads(res.data)
        self.assertEqual(data['message'], 'post added!')


    def test_getPosts(self):
        res = self.app.get('/post')
        data =  json.loads(res.data)
        self.assertEqual(data['message'], 'All posts')

    def test_deletePosts(self):
        res = self.app.delete('/post/1')
        data =  json.loads(res.data)
        self.assertEqual(data['message'], 'post with id 1 is not present')

