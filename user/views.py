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


REGEX_EMAIL         = '[^@]+@[^@]+\.[^@]+'
REGEX_PASSWORD      = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}'
REGEX_DATE_OF_BIRTH = '(19[0-9][0-9]|20\d{2})-(0[0-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])'
REGEX_PHONE_NUMBER  = '(010)(-{1}\d{4}-{1}\d{4})'


class SignUpView(View):
    def post(self, request):
        try:
            data          = json.loads(request.body)
            email         = data['email']
            password      = data['password']
            date_of_birth = data['date_of_birth']
            phone_number  = data['phone_number']

            user_validation = User.objects.filter(kakao_id__isnull=True).filter(email=email)

            if user_validation:
                return JsonResponse({'MESSAGE' : 'ACCOUNT_EXISTS_ALREADY'}, status=400)

            if not re.match(REGEX_EMAIL, email) or not re.match(REGEX_PASSWORD, password):
                return JsonResponse({'MESSAGE' : 'INVALID_EMAIL_OR_PASSWORD'}, status=400)

            if not re.match(REGEX_DATE_OF_BIRTH, date_of_birth):
                return JsonResponse({'MESSAGE' : 'INVALID_DATE_OF_BIRTH'}, status=400)

            if not re.match(REGEX_PHONE_NUMBER, phone_number):
                return JsonResponse({'MESSAGE' : 'INVALID_PHONE_NUMBER'}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User(
                email         = email,
                password      = hashed_password,
                date_of_birth = date_of_birth,
                phone_number  = phone_number,
            ).save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=400)
        except ValueError:
            return ValueErrorTypeChecking(data)


class SignInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            user_validation = User.objects.filter(kakao_id__isnull=True).filter(email=email)

            if not user_validation:
                return JsonResponse({'MESSAGE' : 'INVALID_EMAIL_OR_PASSWORD'}, status=400)

            signed_user =user_validation.get()
            password_validation = bcrypt.checkpw(password.encode('utf-8'), signed_user.password.encode('utf-8'))

            if not password_validation:
                return JsonResponse({'MESSAGE' : 'INVALID_EMAIL_OR_PASSWORD'}, status=400)

            access_token = jwt.encode({'id' : signed_user.id}, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse({'MESSAGE' : 'SUCCESS', 'ACCESS_TOKEN' : access_token}, status=200)
        except ValueError:
            return ValueErrorTypeChecking(data)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=400)


class KakaoSignInView(View):
    def get(self, request):
        client_id    = KAKAO_KEY['REST_API_KEY']
        redirect_uri = "http://127.0.0.1:8000/users/signin/kakao/callback"
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        )

class KakaoSignInCallbackView(View):
    def get(self, request):
        try:
            code          = request.GET.get("code") #토큰 받기 요청에 필요한 인가 코
            client_id     = KAKAO_KEY['REST_API_KEY']
            redirect_uri  = "http://127.0.0.1:8000/users/signin/kakao/callback"
            token_request = requests.get(
                f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
            )
            token_json         = token_request.json()
            kakao_access_token = token_json.get('access_token')
            profile_request    = requests.get(
                "https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"bearer {kakao_access_token}"},
            )
            profile_json  = profile_request.json()  #json 형태로 변환해주는 듯
            kakao_id      = profile_json.get('id')
            kakao_account = profile_json.get('kakao_account')
            kakao_profile = kakao_account.get('profile')
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
        except Exception as e:
            return JsonResponse({'MESSAGE' : str(e)}, status=400)

