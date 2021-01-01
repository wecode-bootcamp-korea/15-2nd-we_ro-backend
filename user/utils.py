import json
import jwt
import bcrypt

from django.http import JsonResponse

from my_settings import SECRET_KEY, ALGORITHM
from user.models import User

def ValueErrorTypeChecking(data):
    if not isinstance(data['email'], str):
        return JsonResponse({'MESSAGE' : 'INVALID_EMAIL_TYPE'}, status=400)

    if not isinstance(data['password'], str):
        return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD_TYPE'}, status=400)

    if not isinstance(data['new_password'], str):
        return JsonResponse({'MESSAGE' : 'INVALID_NEW_PASSWORD_TYPE'}, status=400)

    if not isinstance(data['phone_number'], str):
        return JsonResponse({'MESSAGE' : 'INVALID_PHONE_NUMBER_TYPE'}, status=400)

    if not isinstance(data['new_phone_number'], str):
        return JsonResponse({'MESSAGE' : 'INVALID_NEW_PHONE_NUMBER_TYPE'}, status=400)

    if not isinstance(data['new_image'], str):
        return JsonResponse({'MESSAGE' : 'INVALID_NEW_IMAGE_TYPE'}, status=400)

def SignInAuthorization(function):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization')
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            signed_user  = User.objects.get(id=payload['id'])
            request.user = signed_user
            return function(self, request, *args, **kwargs)
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_USER'}, status=400)
        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE' : 'INVALID_ACCESS_TOKEN'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'SIGN_UP_FIRST'}, status=400)
    return wrapper
