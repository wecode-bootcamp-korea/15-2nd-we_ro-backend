import re
import json
import bcrypt
import jwt
import requests

from django.http      import JsonResponse
from django.views     import View
from django.shortcuts import redirect

from user.models import User
from user.utils  import ValueErrorTypeChecking
from my_settings import SECRET_KEY, ALGORITHM, KAKAO_KEY


class KakaoSignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            kakao_access_token = data['kakao_access_token']
            profile_request    = requests.get(
                "https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"bearer {kakao_access_token}"},
            )
            profile_json  = profile_request.json()
            kakao_id      = profile_json.get('id')
            kakao_account = profile_json.get('kakao_account')
            kakao_email   = kakao_account.get('email')

            user_validation = User.objects.filter(kakao_id=kakao_id)

            if not user_validation:
                User(
                    email    = kakao_email,
                    kakao_id = kakao_id,
                ).save()
                signed_user  = user_validation.get()
                access_token = jwt.encode({'id' : signed_user.id}, SECRET_KEY, algorithm=ALGORITHM)

            else:
                signed_user  = user_validation.get()
                access_token = jwt.encode({'id' : signed_user.id}, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse({'MESSAGE' : 'SUCCESS', 'ACCESS_TOKEN' : access_token}, status=200)
        except KeyError:
                return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=401)

