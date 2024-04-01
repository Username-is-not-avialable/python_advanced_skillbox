from freezegun import freeze_time
import datetime
import unittest
from good_day import app


class TestCorrectWeekday(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello_world/'

    def test_get_correct_weekday(self):
        username = 'Tolya'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)



if __name__ == "__main__":
    unittest.main()