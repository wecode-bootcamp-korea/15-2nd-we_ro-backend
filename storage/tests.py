import jwt
import json
import bcrypt

from django.test  import Client, TestCase
from django.utils import timezone
from django.http import QueryDict, HttpResponse

from my_settings    import SECRET_KEY, ALGORITHM
from user.models    import User, Character
from music.models   import *
from storage.models import Mylist



class MylistViewTest(TestCase):
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

        mylist = Mylist(
            name = timezone.now().strftime('%Y%m%d'),
            character_id=self.character_id
        )

        mylist.save()

        self.mylist = mylist
        self.mylist_id = mylist.id
        self.updated_date = timezone.now().strftime('%Y%m%d')


    def tearDown(self):
        User.objects.all().delete()

    def test_read_mylist_api_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token, 'HTTP_Character' : self.character_id}

        response = client.get('/storage/mylist', content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'MESSAGE' : 'SUCCESS',
                             'RESULTS' : [
                                 {
                                     'mylist_id' : self.mylist.id,
                                     'mylist_name' : self.mylist.name,
                                     'mylist_updated_date' : self.mylist.updated_at.strftime('%Y-%m-%d'),
                                 }]})

    def test_create_mylist_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token, 'HTTP_Character' : self.character_id}

        response = client.post('/storage/mylist', content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})

    def test_delete_mylist_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token, 'HTTP_Character' : self.character_id}

        mylist_id = self.mylist_id

        response = client.delete(f'/storage/mylist/{mylist_id}', content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})

    def test_change_mylist_name_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token, 'HTTP_Character' : self.character_id}

        mylist_id = self.mylist_id

        mylist = {
            'new_name' : '재밌는 노래들'
        }

        response = client.patch(f'/storage/mylist/{mylist_id}', json.dumps(mylist), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})


class MylistMusicViewTest(TestCase):
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
        self.user         = user
        self.user_id      = user.id

        character = Character(
            name = '순대',
            user_id = self.user_id,
        )

        character.save()
        self.character    = character
        self.character_id = character.id

        mylist = Mylist(
            name = timezone.now().strftime('%Y%m%d'),
            character_id=self.character_id
        )

        mylist.save()

        self.mylist = mylist
        self.mylist_id = mylist.id
        self.updated_date = timezone.now().strftime('%Y%m%d')


        album_type = AlbumType(name ='정규')
        album_type.save()
        self.album_type = album_type

        gender = Gender(name = 'Male')
        gender.save()
        self.gender = gender

        genre = Genre(name='국내 발라드')
        genre.save()
        self.genre = genre

        country = Country(name='Korea')
        country.save()
        self.country = country

        artist_type = ArtistType(name='솔로')
        artist_type.save()
        self.artist_type = artist_type

        artist = Artist(
            name              = '김동률',
            artist_type_id    = self.artist_type.id,
            gender_id         = self.gender.id,
            profile_image_url = 'https://dimg.donga.com/wps/NEWS/IMAGE/2019/12/02/98619588.1.jpg',
            genre_id          = self.genre.id
        )
        artist.save()
        self.artist = artist

        album = Album(
            name          = '김동률과 아재들',
            artist_id     = self.artist.id,
            release_date  = '2009-01-23',
            album_type_id = self.album_type.id,
            image_url     = 'https://unsplash.com/photos/pvzlggtEr3U',
            country_id    = self.country.id
        )
        album.save()
        self.album = album

        album_genre = AlbumGenre(
            album_id = self.album.id,
            genre_id = self.genre.id,
        )

        album_genre.save()
        self.album_genre = album_genre

        music = Music(
            name          = '우리가 살아가는 이유',
            streaming_url = 'https://unsplash.com/photos/pvzlggtEr3U',
            album_id      = self.album.id,
            artist_id     = self.artist.id
        )
        music.save()
        self.music = music

        music = Music(
            name          = '배고파.. 졸려',
            streaming_url = 'https://unsplash.com/photos/pvzlggtEr3U',
            album_id      = self.album.id,
            artist_id     = self.artist.id
        )
        music.save()
        self.music = music

    def tearDown(self):
        User.objects.all().delete()
        Music.objects.all().delete()
        Artist.objects.all().delete()
        Music.objects.all().delete()
        AlbumType.objects.all().delete()
        Gender.objects.all().delete()
        Genre.objects.all().delete()
        Country.objects.all().delete()
        ArtistType.objects.all().delete()
        Artist.objects.all().delete()
        Album.objects.all().delete()
        AlbumGenre.objects.all().delete()
        Music.objects.all().delete()


    def test_add_musices_to_mylist_success(self):
        client = Client()

        headers = {'HTTP_Authorization' : self.access_token, 'HTTP_Character' : self.character_id}

        mylist_id = self.mylist_id

        data = {
            'id' : ['1','2']
        }

        response = client.post(f'/storage/mylist/{mylist_id}/music', data, format='multipart',  **headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS'})
