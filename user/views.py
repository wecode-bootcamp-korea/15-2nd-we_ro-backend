import re
import json
import bcrypt
import jwt

from django.http      import JsonResponse
from django.views     import View

from user.models import User, Character
from my_settings import SECRET_KEY, ALGORITHM


REGEX_EMAIL         = '[^@]+@[^@]+\.[^@]+'
REGEX_PASSWORD      = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}'
REGEX_DATE_OF_BIRTH = '(19[0-9][0-9]|20\d{2})-(0[0-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])'
REGEX_PHONE_NUMBER  = '(010)(-{1}\d{4}-{1}\d{4})'

class CharacterCreateView(View):
    def post(self, request, user_id):
        try:
            data = json.loads(request.body)
            name = data['name']
            name_validation = Character.objects.select_related('user').filter(user_id=user_id).filter(name=name)

            if name_validation:
                return JsonResponse({'MESSAGE' : 'CHARACTER_NAME_EXISTS'}, status=400)

            Character(
                user_id = user_id,
                name    = name,
            ).save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=400)
        except ValueError:
            return JsonResponse({'MESSAGE' : 'INVALID_VALUE'}, status=400)


class CharacterNameChangeView(View):
    def patch(self, request, user_id, character_id):
        try:
            data = json.loads(request.body)
            new_name = data['new_name']

            character = Character.objects.filter(user_id=user_id).filter(character_id=character_id).get()

            character.name = new_name
            character.save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=400)
        except ValueError:
            return JsonResponse({'MESSAGE' : 'INVALID_VALUE'}, status=400)


class CharacterImageChangeView(View):
    def patch(self, request, user_id, character_id):
        try:
            data = json.loads(request.body)
            new_profile_image_url = data['new_profile_image_url']

            character = Character.objects.filter(user_id=user_id).filter(character_id=character_id).get()

            character.profile_image_url = new_profile_image_url
            character.save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE' ; 'INVALID_KEY'}, status=400)
        except ValueError:
            return JsonResponse({'MESSAGE' : 'INVALID_VALUE'}, status=400)





