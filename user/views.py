import re
import json
import bcrypt
import jwt
import requests

from django.http      import JsonResponse
from django.views     import View
from django.shortcuts import redirect

from user.models import User
from user.utils  import SignInAuthorization, ValueErrorTypeChecking, CharacterAuthorization
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


class CharacterView(View):
    @SignInAuthorization
    @CharacterAuthorization
    def get(self, request):
        try:
            signed_user = request.user
            characters  = Character.objects.filter(user_id=signed_user.id).all()

            results =[
                {
                    'id' : character.id,
                    'name' : character.name,
                    'profile_image_url' : character.profile_image_url,
                }
                for character in characters
            ]
            return JsonResponse({'MESSAGE' : 'SUCCESS', 'RESULTS' : results}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=400)
        except ValueError:
            return ValueErrorTypeChecking(data)

    @SignInAuthorization
    @CharacterAuthorization
    def post(self, request):
        data = json.loads(request.body)
        try:
            name        = data['name']
            signed_user = request.user

            if Character.objects.filter(user_id=signed_user.id).filter(name=name).exists():
                return JsonResponse({'MESSAGE' : 'CHARACTER_NAME_EXISTS'}, status=400)

            Character(
                user_id = signed_user.id,
                name    = name,
            ).save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=400)
        except ValueError:
            return ValueErrorTypeChecking(data)

    @SignInAuthorization
    @CharacterAuthorization
    def delete(self, request, character_id):
        try:
            signed_user = request.user

            character = Character.objects.filter(user_id=signed_user.id).filter(id=character_id).get()

            character.delete()
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'CHARACTER_DOES_NOT_EXIST'}, status=402)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=401)

    @SignInAuthorization
    @CharacterAuthorization
    def patch(self, request, character_id):
        data = json.loads(request.body)
        try:
            new_name    = data.get('new_name')
            new_image   = data.get('new_image')
            signed_user = request.user

            if Character.objects.filter(user_id=signed_user.id).filter(id=character_id).exists():
                character = Character.objects.get(id=character_id, user_id=signed_user.id)

            if new_name is not None:
                character.name = new_name

            if new_image is not None:
                character.image = new_image

            character.save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_CHARACTER'}, status=400)
        except ValueError:
            return ValueErrorTypeChecking()


class TasteChartView(View):
    @SignInAuthorization
    @CharacterAuthorization
    def post(self, request):
        try:
            signed_character = request.character

            taste_data = json.loads(request.body)

            chart_list = taste_data['id']

            for chart in chart_list:
                if not CharacterTasteChart.objects.filter(character_id=signed_character.id).filter(chart_id=int(chart)):
                    CharacterTasteChart(
                        character_id = signed_character.id,
                        chart_id    = Chart.objects.get(id=int(chart)).id
                    ).save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except Chart.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_CHART'}, status=400)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_CHARACTER'}, status=400)
        except ValueError:
            return JsonResponse({'MESSAGE' : 'INVALID_VALUE_ID_MUST_BE_INT'}, status=400)

    @SignInAuthorization
    @CharacterAuthorization
    def get(self, request):
        try:
           signed_character = request.character

           taste_chart_list = CharacterTasteChart.objects.select_related('chart').filter(character_id=signed_character.id)

           results = [
               {
                   'chart_id' : taste.chart.id,
                   'chart_name' : taste.chart.name,
               }
               for taste in taste_chart_list
           ]
           return JsonResponse({'MESSAGE' : 'SUCCESS', 'RESULTS' : results}, status=200)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_CHARACTER'}, status=400)
        except Chart.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_CHART'}, status=400)

class TasteGenreView(View):
    @SignInAuthorization
    @CharacterAuthorization
    def post(self, request):
        try:
            signed_character = request.character

            taste_data = json.loads(request.body)

            genre_list = taste_data['id']

            for genre in genre_list:
                if not CharacterTasteGenre.objects.filter(character_id=signed_character.id).filter(genre_id=int(genre)):
                    CharacterTasteGenre(
                        character_id = signed_character.id,
                        genre_id    = Genre.objects.get(id=int(genre)).id
                    ).save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except Genre.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_GENRE'}, status=400)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_CHARACTER'}, status=400)
        except ValueError:
            return JsonResponse({'MESSAGE' : 'INVALID_VALUE_ID_MUST_BE_INT'}, status=400)

    @SignInAuthorization
    @CharacterAuthorization
    def get(self, request):
        try:
            signed_character = request.character

            taste_genre_list = CharacterTasteGenre.objects.select_related('genre').filter(character_id=signed_character.id)

            results = [
                {
                    'genre_id' : taste.genre.id,
                    'genre_name' : taste.genre.name,
                }
                for taste in taste_genre_list
            ]
            return JsonResponse({'MESSAGE' : 'SUCCESS', 'RESULTS' : results}, status=200)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_CHARACTER'}, status=400)
        except Genre.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_GENRE'}, status=400)


class TasteArtistView(View):
    @SignInAuthorization
    @CharacterAuthorization
    def post(self, request):
        try:
            signed_character = request.character

            taste_data = json.loads(request.body)

            artist_list = taste_data['id']

            for artist in artist_list:
                if not CharacterTasteArtist.objects.filter(character_id=signed_character.id).filter(artist_id=int(artist)):
                    CharacterTasteArtist(
                        character_id = signed_character.id,
                        artist_id    = Artist.objects.get(id=int(artist)).id
                    ).save()

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)
        except Artist.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_ARIST'}, status=400)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_CHARACTER'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE' : 'INVALID_KEY'}, status=400)

    @SignInAuthorization
    @CharacterAuthorization
    def get(self, request):
        try:
            signed_character = request.character

            taste_artist_list = CharacterTasteArtist.objects.select_related('artist').filter(character_id=signed_character.id)

            results = [
                {
                    'artist_id' : taste.artist.id,
                    'artist_name' : taste.artist.name,
                    'artist_image_url' : taste.artist.profile_image_url
                }
                for taste in taste_artist_list
            ]
            return JsonResponse({'MESSAGE' : 'SUCCESS', 'RESULTS' : results}, status=200)
        except Character.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_CHARACTER'}, status=400)
        except Artist.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'INVALID_ARTIST'}, status=400)
