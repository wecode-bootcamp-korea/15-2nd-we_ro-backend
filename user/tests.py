import json
import bcrypt

from django.test import Client
from django.test import TestCase

from user.models import User, Platform


class UserTest(TestCase):
    def setUp(self):
        Platform.objects.create(name='kakao')
        Platform.objects.create(name='flo')
        User.objects.create(
            email = 'kst6294@gmail.com',
            password = '123qwe!@#QWE',
            date_of_birth = '1991-09-04',
            phone_number = '010-1234-1234',
            platform_id = Platform.objects.get(name='kakao').id
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_signupview_post_create_success_with_no_duplicated_user(self):
        client = Client()
        user = {
            'email' : 'suntae@gmail.com',
            'password' : '123qwe!@#QWE',
            'date_of_birth' : '1991-09-04',
            'phone_number' : '010-1234-1234',
            'platform' : 'flo'
        }
        response = client.post('/users/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_signupview_post_create_success_with_duplicated_user_no_duplicated_platform(self):
        client = Client()
        user = {
            'email' : 'kst6294@gmail.com',
            'password' : '123qwe!@#QWE',
            'date_of_birth' : '1991-09-04',
            'phone_number' : '010-1234-1234',
            'platform' : 'flo'
        }
        response = client.post('/users/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_signupview_post_create_fail_with_duplicated_user(self):
        client = Client()
        user = {
            'email' : 'kst6294@gmail.com',
            'password' : '123qwe!@#QWE',
            'date_of_birth' : '1991-09-04',
            'phone_number' : '010-1234-1234',
            'platform' : 'kakao'
        }
        response = client.post('/users/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)

