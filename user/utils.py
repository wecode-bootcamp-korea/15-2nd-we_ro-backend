import json
import jwt
import bcrypt

from django.http import JsonResponse

from my_settings import SECRET_KEY, ALGORITHM
from user.models import User

def ValueErrorTypeChecking(data):
    if type(data['email']) != str:
        return JsonResponse({'MESSAGE' : 'INVALID_EMAIL_TYPE'}, status=400)

    if type(data['password']) != str:
        return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD_TYPE'}, status=400)

def SignInAuthorization(function):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token    = request.headers.get('Authorization')
            payload         = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            signed_user     = User.objects.get(id=payload['user_id'])
            request.user_id = signed_user.id
            return function(self, request, *args, **kwargs)
        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE' : 'INVALID_ACCESS_TOKEN'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'SIGN_UP_FIRST'}, status=400)
    return wrapper


def ValueErrorTypeChecking(data):
    if type(data['email']) != str:
        return JsonResponse({'MESSAGE' : 'INVALID_EMAIL_TYPE'}, status=400)

    if type(data['password']) != str:
        return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD_TYPE'}, status=400)
