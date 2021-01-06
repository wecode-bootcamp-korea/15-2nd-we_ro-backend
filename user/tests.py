import jwt
import json
import bcrypt
import jwt
import requests

from unittest.mock import patch, MagicMock

from django.test   import Client, TestCase

from user.models   import User, Character, CharacterTasteGenre, CharacterTasteArtist, CharacterTasteChart
from music.models  import Genre, Gender, ArtistType, Artist, Album, Chart
from my_settings   import SECRET_KEY, ALGORITHM
from unittest.mock import patch, MagicMock


class CharacterTasteView(TestCase):
    def setUp(self):
        password        = '123qwe!@#QWE'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        user = User(
            email         = 'kst6294@gmail.com',
            password      = hashed_password,
            date_of_birth = '1991-09-04',
            phone_number  = '010-1234-1234',
        )

        user.save()
        self.access_token = jwt.encode({'id' : User.objects.get(id=user.id).id}, SECRET_KEY, algorithm=ALGORITHM)
        self.user    = user
        self.user_id = user.id

        character = Character(
            name = '순대',
            user_id = self.user_id,
        )

        character.save()
        self.character    = character
        self.character_id = character.id


        artist_type = ArtistType(name='그룹')
        artist_type.save()
        self.artist_type = artist_type

        gender = Gender(name='여성')
        gender.save()
        self.gender = gender

        genre = Genre(
            name = '발라드'
        )
        genre.save()
        self.genre = genre


        artist = Artist(
            name              = '다비치',
            profile_image_url = 'http://www.google.co.kr',
            artist_type_id    = self.artist_type.id,
            gender_id         = self.gender.id,
            genre_id          = self.genre.id
        )
        artist.save()
        self.artist = artist

        chart = Chart(
            name = '빌보드 차트'
        )
        chart.save()
        self.chart = chart

        character_taste_artist = CharacterTasteArtist(
            artist_id    = self.artist.id,
            character_id = self.character_id
        )
        character_taste_artist.save()
        self.character_taste_artist = character_taste_artist

        character_taste_genre = CharacterTasteGenre(
            genre_id          = self.genre.id,
            character_id      = self.character_id
        )
        character_taste_genre.save()
        self.character_taste_genre = character_taste_genre


        character_taste_chart = CharacterTasteChart(
            chart_id     = self.chart.id,
            character_id = self.character_id
        )
        character_taste_chart.save()
        self.character_taste_chart = character_taste_chart

    def tearDown(self):
        User.objects.all().delete()
        ArtistType.objects.all().delete()
        Gender.objects.all().delete()
        Genre.objects.all().delete()
        Chart.objects.all().delete()
        Character.objects.all().delete()

    def test_add_artist_list_to_character_taste_artist_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token, 'HTTP_Character' : self.character_id}

        artist_list = {
            'id' : [f'{self.artist.id}']
        }

        response = client.post('/users/taste/artist', artist_list, format='multipart',  **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})

    def test_add_genre_list_to_character_taste_genre_success(self):
        client = Client()
        headers = {'HTTP_Authorization' : self.access_token, 'HTTP_Character' : self.character_id}
>>>>>>> d12d58f... Add: Taste 취향관리 기능 구현

        genre_list = {
            'id' : [f'{self.genre.id}']
        }

        response = client.post('/users/taste/genre', genre_list, format='multipart',  **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})

    def test_add_chart_list_to_character_taste_chart_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token, 'HTTP_Character' : self.character_id}

        chart_list = {
            'id' : [f'{self.chart.id}']
        }

        response = client.post('/users/taste/chart', chart_list, format='multipart',  **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})


    def test_read_character_taste_artist_api_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token, 'HTTP_Character' : self.character_id}

        response = client.get('/users/taste/chart', contet_type='application/json',  **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS', 'RESULTS' : [
            {
                'chart_id'   : self.chart.id,
                'chart_name' : self.chart.name
            }]})

    def test_read_character_taste_genre_api_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token, 'HTTP_Character' : self.character_id}

        response = client.get('/users/taste/genre', contet_type='application/json',  **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS', 'RESULTS' : [
            {
                'genre_id'   : self.genre.id,
                'genre_name' : self.genre.name}
        ]})



    def test_read_character_taste_chart_api_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token, 'HTTP_Character' : self.character_id}

        response = client.get('/users/taste/chart', contet_type='application/json',  **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS', 'RESULTS' : [
            {
                'chart_id'   : self.chart.id,
                'chart_name' : self.chart.name
            }]})
