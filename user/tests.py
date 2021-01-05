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

        response = client.post('/users/kakao-signup', json.dumps(kakao_access_token), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS', 'ACCESS_TOKEN' : response.json()['ACCESS_TOKEN']})


