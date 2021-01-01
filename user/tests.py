import json
import bcrypt
import jwt

from django.test   import Client, TestCase

from user.models   import User
from my_settings   import SECRET_KEY, ALGORITHM
from unittest.mock import patch, MagicMock

class UserSignUpTest(TestCase):
    def setUp(self):
        password        = '123qwe!@#QWE'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        User(
            email         = 'kst6294@gmail.com',
            password      = hashed_password,
            date_of_birth = '1991-09-04',
            phone_number  = '010-1234-1234',
        ).save()

    def tearDown(self):
        User.objects.all().delete()

    def test_signupview_post_create_success_with_no_duplicated_user(self):
        client = Client()
        user = {
            'email'         : 'suntae@gmail.com',
            'password'      : '123qwe!@#QWE',
            'date_of_birth' : '1991-09-04',
            'phone_number'  : '010-1234-1234',
        }

        response = client.post('/users/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_signupview_post_create_fail_with_duplicated_user(self):
        client = Client()
        user = {
            'email'         : 'kst6294@gmail.com',
            'password'      : '123qwe!@#QWE',
            'date_of_birth' : '1991-09-04',
            'phone_number'  : '010-1234-1234',
        }

        response = client.post('/users/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)


class UserSignInTest(TestCase):
    def setUp(self):
        password        = '123qwe!@#QWE'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        User(
            email         = 'kst6294@gmail.com',
            password      = hashed_password,
            date_of_birth = '1991-09-04',
            phone_number  = '010-1234-1234',
        ).save()

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

        response = client.post('/users/signin', json.dumps(user), content_type='application/json')
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

        response = client.post('/users/signin', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'MESSAGE' : 'INVALID_EMAIL_OR_PASSWORD'})

class UserPasswordCheckTest(TestCase):
    def setUp(self):
        password        = '123qwe!@#QWE'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        user = User(
            email         = 'kst6294@gmail.com',
            password      = hashed_password,
            date_of_birth = '1991-09-04',
            phone_number  = '010-1234-1234',
        )

        user.save()

        self.access_token = jwt.encode({'id' : User.objects.get(id=user.id).id}, SECRET_KEY, algorithm=ALGORITHM)
        self.user_id      = user.id

    def tearDown(self):
        User.objects.all().delete()

    def test_password_is_same_check_post_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token}

        user = {
            'user_id' : self.user_id,
            'password' : '123qwe!@#QWE',
        }

        response = client.post('/users/password/check', json.dumps(user), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})

    def test_password_is_same_check_post_fail(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token}

        user = {
            'user_id' : self.user_id,
            'password' : '23eewre!@#QWE',
        }

        response = client.post('/users/password/check', json.dumps(user), content_type='application/json', **headers)


        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'MESSAGE' : 'PASSWORD_IS_DIFFERENT'})

class UserPasswordChangeTest(TestCase):
    def setUp(self):
        password        = '123qwe!@#QWE'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        user = User(
            email         = 'kst6294@gmail.com',
            password      = hashed_password,
            date_of_birth = '1991-09-04',
            phone_number  = '010-1234-1234',
        )

        user.save()

        self.access_token = jwt.encode({'id' : User.objects.get(id=user.id).id}, SECRET_KEY, algorithm=ALGORITHM)
        self.user_id      = user.id

    def tearDown(self):
        User.objects.all().delete()

    def test_password_change_old_password_to_new_passowrd_post_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token}

        user = {
            'user_id'      : self.user_id,
            'new_password' : '2sdf#223QWE!@#',
        }

        response = client.patch('/users/password/change', json.dumps(user), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})


class UserPhoneNumberChangeTest(TestCase):
    def setUp(self):
        password        = '123qwe!@#QWE'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        user = User(
            email         = 'kst6294@gmail.com',
            password      = hashed_password,
            date_of_birth = '1991-09-04',
            phone_number  = '010-1234-1234',
        )

        user.save()

        self.access_token = jwt.encode({'id' : User.objects.get(id=user.id).id}, SECRET_KEY, algorithm=ALGORITHM)
        self.user_id      = user.id

    def tearDown(self):
        User.objects.all().delete()

    def test_phone_number_change_old_phone_number_to_new_phone_number_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token}

        user = {
            'user_id' : self.user_id,
            'new_phone_number' : '010-4321-4321',
        }

        response = client.patch('/users/phonenumber/change', json.dumps(user), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})
