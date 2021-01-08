import re
import json

from django.http  import JsonResponse
from django.views import View
from django.utils import timezone

from user.utils     import ValueErrorTypeChecking, SignInAuthorization, CharacterAuthorization
from user.models    import Character
from storage.models import Mylist, MylistMusic
from music.models   import Music


class MylistView(View):
    @SignInAuthorization
    @CharacterAuthorization
    def get(self, request):
        try:
            signed_character = request.character
            mylists          = Mylist.objects.filter(character_id=signed_character.id)

            results = [
                {
                    'mylist_id' : mylist.id,
                    'mylist_name' : mylist.name,
                    'mylist_updated_date' : mylist.updated_at.strftime('%Y-%m-%d'),
                } for mylist in mylists
            ]

            return JsonResponse({'MESSAGE' : 'SUCCESS', 'RESULTS' : results}, status=200)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'CHARACTER_DOES_NOT_EXIST'}, status=400)
        except Mylist.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'CHARACTER_DOES_NOT_EXIST'}, status=400)

    @SignInAuthorization
    @CharacterAuthorization
    def post(self, request):
        try:
            signed_user      = request.user
            signed_character = request.character

            Mylist(
                name = timezone.now().strftime('%Y%m%d'),
                character_id = signed_character.id,
            ).save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'CHARACTER_DOES_NOT_EXIST'}, status=400)
        except Mylist.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'MYLIST_DOES_NOT_EXIST'}, status=400)

    @SignInAuthorization
    @CharacterAuthorization
    def delete(self, request, mylist_id):
        try:
            signed_character = request.character

            Mylist.objects.filter(character_id=signed_character.id).filter(id=mylist_id).get().delete()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'CHARACTER_DOES_NOT_EXIST'}, status=400)
        except Mylist.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'MYLIST_DOES_NOT_EXIST'}, status=400)

    @SignInAuthorization
    @CharacterAuthorization
    def patch(self, request, mylist_id):
        data = json.loads(request.body)
        try:
            new_name         = data['new_name']
            signed_character = request.character

            mylist      = Mylist.objects.filter(character_id=signed_character.id).filter(id=mylist_id).get()
            mylist.name = new_name

            mylist.save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except ValueError:
            return ValueErrorTypeChecking(data)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'})
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'CHARACTER_DOES_NOT_EXIST'}, status=400)
        except Mylist.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'MYLIST_DOES_NOT_EXIST'}, status=400)


class MylistMusicView(View):
    @SignInAuthorization
    @CharacterAuthorization
    def post(self, request, mylist_id):
        try:
            data = json.loads(request.body)

            music_list = data['id']

            mylist_music = MylistMusic.objects.filter(mylist_id=mylist_id)

            for music in music_list:
                if not mylist_music.filter(music_id=int(music)):
                    MylistMusic(
                        music_id  = Music.objects.get(id=int(music)).id,
                        mylist_id = mylist_id,
                    ).save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except Music.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'MUSIC_DOES_NOT_EXIST'}, status=400)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'CHARACTER_DOES_NOT_EXIST'}, status=400)
        except Mylist.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'MYLIST_DOES_NOT_EXIST'}, status=400)

    @SignInAuthorization
    @CharacterAuthorization
    def get(self, request, mylist_id):
        try:
            signed_character = request.character

            mylist_music = MylistMusic.objects.filter(mylist__character_id=signed_character.id, mylist_id=mylist_id).select_related('music', 'music__artist', 'music__album')
            results = [
                {
                    'music_id'   : mylist.music.id,
                    'music_name' : mylist.music.name,
                    'music_artist' : mylist.music.album.name,
                    'music_image' : mylist.music.album.image_url,
                } for mylist in mylist_music.all()]

            return JsonResponse({'MESSAGE' : 'SUCCESS', 'RESULTS' : results}, status=200)
        except Music.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'MUSIC_DOES_NOT_EXIST'}, status=400)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'CHARACTER_DOES_NOT_EXIST'}, status=400)
        except Mylist.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'MYLIST_DOES_NOT_EXIST'}, status=400)




