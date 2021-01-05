import jwt
import json
import bcrypt
import jwt
import requests

from unittest.mock import patch, MagicMock

from django.test   import Client, TestCase

from user.models import User, Character
from my_settings import SECRET_KEY, ALGORITHM


class KakaoSignInTest(TestCase):
    def setUp(self):
        client = Client()

    @patch('user.views.requests')
    def test_user_sign_in_kakao_post_success(self, mock_request):
        class FakeResponse:
            def json(self):
                return {
                    'id' : 1287128794,
                    'kakao_account' :
                    {
                        'email' : 'suntaekim@kakao.com'
                    }
                }

        kakao_access_token = {'kakao_access_token' : 1231247723}

        client = Client()

        mock_request.get = MagicMock(return_value=FakeResponse())
        headers = {'HTTP_Authorization' : self.access_token}

        user = {
            'user_id'      : self.user_id,
            'new_password' : '2sdf#223QWE!@#',
        }

        character_id = self.character_id

        character = {
            'new_name' : '강아지,'
        }

        response = client.patch(f'/users/character/{character_id}',json.dumps(character), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})


class CharacterViewTest(TestCase):
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
        self.user    = user
        self.user_id = user.id

        character = Character(
            name = '사장님',
            user_id = self.user_id,
        )

        character.save()
        self.character    = character
        self.character_id = character.id


    def tearDown(self):
        User.objects.all().delete()

    def test_character_read_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token}

        response = client.get('/users/character', content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS', 'RESULTS' : [
            {
                'id' : self.character_id,
                'name' : self.character.name,
                'profile_image_url' : '',
            }
        ]})

    def test_character_create_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token}

        character = {
            'name' : '순대',
        }

        response = client.post('/users/character', json.dumps(character), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})

    def test_character_delete_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token}

        character_id = self.character_id

        response = client.delete(f'/users/character/{character_id}', content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})


    def test_character_update_name_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token}

        character_id = self.character_id

        character = {
            'new_name' : '강아지,'
        }

        response = client.patch(f'/users/character/{character_id}',json.dumps(character), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})


    def test_character_update_image_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token}

        character_id = self.character_id

        character = {
            'new_profile_image_url' : 'http://www.google.co.kr',
        }

        response = client.post('/users/kakao-signup', json.dumps(kakao_access_token), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS', 'ACCESS_TOKEN' : response.json()['ACCESS_TOKEN']})


