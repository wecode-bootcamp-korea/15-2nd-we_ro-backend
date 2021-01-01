import re
import json
import bcrypt
import jwt
import requests

from django.http      import JsonResponse
from django.views     import View

from user.models import User
from user.utils  import SignInAuthorization, ValueErrorTypeChecking
from my_settings import SECRET_KEY, ALGORITHM


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
        data     = json.loads(request.body)
        try:
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
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_USER'}, status=400)
        except ValueError:
            return ValueErrorTypeChecking(data)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=400)


class PasswordCheckView(View):
    @SignInAuthorization
    def post(self, request):
        data = json.loads(request.body)
        try:
            user_id      = data['user_id']
            password     = data['password']
            signed_user  = User.objects.get(id=user_id)

            password_validation = bcrypt.checkpw(password.encode('utf-8'), signed_user.password.encode('utf-8'))

            if not password_validation:
                return JsonResponse({'MESSAGE' : 'PASSWORD_IS_DIFFERENT'}, status=400)
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except ValueError:
            return ValueErrorTypeChecking(data)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=400)


class PasswordChangeView(View):
    @SignInAuthorization
    def patch(self, request):
        data = json.loads(request.body)
        try:
            new_password = data['new_password']
            signed_user  = request.user

            password_validation = bcrypt.checkpw(new_password.encode('utf-8'), signed_user.password.encode('utf-8'))

            if password_validation:
                return JsonResponse({'MESSAGE' : 'PASSWORD_IS_SAME'}, status=400)

            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            signed_user.password = hashed_password
            signed_user.save()
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except ValueError:
            return ValueErrorTypeChecking(data)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=400)


class PhonenumberChangeView(View):
    @SignInAuthorization
    def patch(self, request):
        data = json.loads(request.body)
        try:
            new_phone_number = data['new_phone_number']
            signed_user  = request.user

            if new_phone_number == signed_user.phone_number:
                return JsonResponse({'MESSAGE' : 'PHONE_NUMBER_IS_SAME'}, status=400)

            signed_user.phone_number = new_phone_number
            signed_user.save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except ValueError:
            return ValueErrorTypeChecking(data)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=400)
