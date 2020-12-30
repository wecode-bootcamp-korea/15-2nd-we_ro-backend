import json

from django.http import JsonResponse

def ValueErrorTypeChecking(data):
    if type(data['email']) != str:
        return JsonResponse({'MESSAGE' : 'INVALID_EMAIL_TYPE'}, status=400)

    if type(data['password']) != str:
        return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD_TYPE'}, status=400)

