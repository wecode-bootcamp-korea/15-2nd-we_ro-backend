import json
import bcrypt
import jwt

from django.test      import Client
from django.test      import TestCase

from user.models import User
from my_settings import SECRET_KEY, ALGORITHM

class UserSignUpTest(TestCase):
    def setUp(self):
        password = '123qwe!@#QWE'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        User(
            email = 'kst6294@gmail.com',
            password = hashed_password,
            date_of_birth = '1991-09-04',
            phone_number = '010-1234-1234',
        ).save()

    def tearDown(self):
        User.objects.all().delete()

    def test_signupview_post_create_success_with_no_duplicated_user(self):
        client = Client()
        user = {
            'email' : 'suntae@gmail.com',
            'password' : '123qwe!@#QWE',
            'date_of_birth' : '1991-09-04',
            'phone_number' : '010-1234-1234',
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
        }

        response = client.post('/users/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)


class UserSignInTest(TestCase):
    def setUp(self):
        password = '123qwe!@#QWE'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        User(
            email = 'kst6294@gmail.com',
            password      = hashed_password,
            date_of_birth = '1991-09-04',
            phone_number  = '010-1234-1234',
        ).save()

        email         = 'kst6294@gmail.com'
        password      = '123qwe!@#QWE'
        date_of_birth = '1991-09-04'
        phone_number  = '010-1234-1234'

    def tearDown(self):
        User.objects.all().delete()

    def test_signinview_post_success_with_user(self):
        client = Client()
        user = {
            'email'         : 'kst6294@gmail.com',
            'password'      : '123qwe!@#QWE',
            'date_of_birth' : '1991-09-04',
            'phone_number'  : '010-1234-1234',
        }
        response     = client.post('/users/signin', json.dumps(user), content_type='application/json')
        access_token = response.json()['ACCESS_TOKEN']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS', 'ACCESS_TOKEN' : access_token})

    def test_signinview_post_fail_with_no_user(self):
        client = Client()
        user = {
            'email'         : 'suntae@gmail.com',
            'password'      : '123qwe!@#QWE',
            'date_of_birth' : '1991-09-04',
            'phone_number'  : '010-1234-1234',
        }
        response     = client.post('/users/signin', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'MESSAGE' : 'INVALID_EMAIL_OR_PASSWORD'})

    def test_signinview_post_fail_INVALID_PASSWORD(self):
        client = Client()
        user = {
            'email'         : 'kst6294@gmail.com',
            'password'      : '123qwe!@#QE',
            'date_of_birth' : '1991-09-04',
            'phone_number'  : '010-1234-1234',
        }

        response        = client.post('/users/signin', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'MESSAGE' : 'INVALID_EMAIL_OR_PASSWORD'})

