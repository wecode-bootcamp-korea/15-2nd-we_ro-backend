from django.test import TestCase, TransactionTestCase, Client
from django.views import View
from django.http import JsonResponse
from django.db.models import Prefetch, Sum
from .models import AlbumType, Gender, Genre, Country, ArtistType, Artist, Album, AlbumGenre, Music, MusicDetail


class MusicInfoTest(TestCase):
    def setUp(self):
        client = Client()
        AlbumType.objects.create(
            id=1,
            name='정규',
        )
        Gender.objects.create(
            id=1,
            name='Male',
        )
        Genre.objects.create(
            id=1,
            name='국내 발라드',
        )
        Country.objects.create(id=1, name='Korea')
        ArtistType.objects.create(id=1, name='솔로')
        Artist.objects.create(
            id=1,
            name='김동률',
            artist_type=ArtistType.objects.get(id=1),
            gender=Gender.objects.get(id=1),
            profile_image_url='https://dimg.donga.com/wps/NEWS/IMAGE/2019/12/02/98619588.1.jpg',
            genre = Genre.objects.get(id=1))
        Album.objects.create(
            id=1,
            name='김동률과 아재들',
            artist=Artist.objects.get(id=1),
            release_date='2009-01-23',
            album_type=AlbumType.objects.get(id=1),
            image_url='https://unsplash.com/photos/pvzlggtEr3U',
            country=Country.objects.get(id=1)
        )
        AlbumGenre.objects.create(id=1,
        album=Album.objects.get(id=1),
        genre=Genre.objects.get(id=1))
        Music.objects.create(
            id=1,
            name='우리가 살아가는 이유',
            streaming_url='https://unsplash.com/photos/pvzlggtEr3U',
            album=Album.objects.get(id=1),
            artist=Artist.objects.get(id=1))
        MusicDetail.objects.create(music=Music.objects.get(id=1),
        lyric='배고프다 하지마',
        play_count='93991')

    def tearDown(self):
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
        MusicDetail.objects.all().delete()

    def test_musicinfo_get_success(self):
        client = Client()
        response = client.get('/music/info')

        musics = Music.objects.all()
        music_info = [{
            'rank': music.id,
            'title': music.name,
            'country': music.album.country.name,
            'url': music.streaming_url,
            'imgUrl': music.album.image_url,
            'album': music.album.name,
            'artist': music.artist.name,
            'rated_r': music.musicdetail.is_rated_r,
            'popularity': music.musicdetail.play_count,
            'lyric': music.musicdetail.lyric,
            'artist_type': music.artist.artist_type.name,
            'artist_gender': music.artist.gender.name,
            'genre': music.album.genre.name,
        } for music in musics]

        self.assertEqual(response.json(), {'MusicInfo': music_info})
        self.assertEqual(response.status_code, 200)

    def test_musicinfo_get_fail(self):

        client   = Client()
        response = self.client.get('/music/infol')
        self.assertEqual(response.status_code, 404)


class CountryMusicTest(TestCase):
    maxDiff = None

    def setUp(self):
        client = Client()
        AlbumType.objects.create(
            id=1,
            name='정규',
        )
        Gender.objects.create(
            id=1,
            name='Male',
        )
        Genre.objects.create(
            id=1,
            name='국내 발라드',
        )
        Country.objects.create(id=1, name='Korea')
        ArtistType.objects.create(id=1, name='솔로')
        Artist.objects.create(
            id=1,
            name='김동률',
            artist_type=ArtistType.objects.get(id=1),
            gender=Gender.objects.get(id=1),
            profile_image_url='https://dimg.donga.com/wps/NEWS/IMAGE/2019/12/02/98619588.1.jpg',
            genre = Genre.objects.get(id=1))
        Album.objects.create(
            id=1,
            name='김동률과 아재들',
            artist=Artist.objects.get(id=1),
            release_date='2009-01-23',
            album_type=AlbumType.objects.get(id=1),
            image_url='https://unsplash.com/photos/pvzlggtEr3U',
            country=Country.objects.get(id=1)
        )
        AlbumGenre.objects.create(id=1,
        album=Album.objects.get(id=1),
        genre=Genre.objects.get(id=1))
        Music.objects.create(
            id=1,
            name='우리가 살아가는 이유',
            streaming_url='https://unsplash.com/photos/pvzlggtEr3U',
            album=Album.objects.get(id=1),
            artist=Artist.objects.get(id=1))
        MusicDetail.objects.create(music=Music.objects.get(id=1),
        lyric='배고프다 하지마',
        play_count='93991')

    def tearDown(self):
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
        MusicDetail.objects.all().delete()

    def test_countrymusic_get_success(self):
        client = Client()
        response = self.client.get('/music/country/1')
        country_id=1
        musics= Music.objects.filter(id__in = Album.objects.filter(country = country_id)).select_related('album', 'artist', 'musicdetail').order_by('-musicdetail__play_count')

        music_list=[
                {
                    'id':            music.id,
                    'title':         music.name,
                    'country':       music.album.country.name,
                    'url':           music.streaming_url,
                    'imgUrl':        music.album.image_url,
                    'album':         music.album.name,
                    'artist':        music.artist.name,
                    'rated_r':       music.musicdetail.is_rated_r,
                    'popularity':    music.musicdetail.play_count,
                    'lyric':         music.musicdetail.lyric,
                    'artist_type':   music.artist.artist_type.name,
                    'artist_gender': music.artist.gender.name,
                    'genre':         music.album.genre.name,
                    'emotion':       music.album.emotion.name,
                    'mood':          music.album.mood.name,
                    'chart':         music.album.chart.name,
                }for music in musics]

        self.assertEqual(response.json(), {'Music_info': music_list})
        self.assertEqual(response.status_code, 200)

class ArtistInfoTest(TestCase):
    maxDiff = None

    def setUp(self):
        client = Client()
        AlbumType.objects.create(
            id=1,
            name='정규',
        )
        Gender.objects.create(
            id=1,
            name='Male',
        )
        Genre.objects.create(
            id=1,
            name='국내 발라드',
        )
        Country.objects.create(id=1, name='Korea')
        ArtistType.objects.create(id=1, name='솔로')
        Artist.objects.create(
            id=1,
            name='김동률',
            artist_type=ArtistType.objects.get(id=1),
            gender=Gender.objects.get(id=1),
            profile_image_url='https://dimg.donga.com/wps/NEWS/IMAGE/2019/12/02/98619588.1.jpg',
            genre = Genre.objects.get(id=1))
        Album.objects.create(
            id=1,
            name='김동률과 아재들',
            artist=Artist.objects.get(id=1),
            release_date= '2009-1-23',
            album_type=AlbumType.objects.get(id=1),
            image_url='https://unsplash.com/photos/pvzlggtEr3U',
            country=Country.objects.get(id=1)
        )
        AlbumGenre.objects.create(id=1,
        album=Album.objects.get(id=1),
        genre=Genre.objects.get(id=1))
        Music.objects.create(
            id=1,
            name='우리가 살아가는 이유',
            streaming_url='https://unsplash.com/photos/pvzlggtEr3U',
            album=Album.objects.get(id=1),
            artist=Artist.objects.get(id=1))
        MusicDetail.objects.create(music=Music.objects.get(id=1),
        lyric='배고프다 하지마',
        play_count='93991')

    def tearDown(self):
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
        MusicDetail.objects.all().delete()

    def test_artistinfo_get_success(self):
        client = Client()
        response = self.client.get('/music/artist/info')

        artists = Artist.objects.select_related('artist_type','gender','genre').prefetch_related('album_set', 'music_set','music_set__musicdetail').annotate(total_play_count=Sum('music__musicdetail__play_count'))

        artist_info = [
            {
                    'name':   artist.name,
                    'image':  artist.profile_image_url,
                    'type':   artist.artist_type.name,
                    'gender': artist.gender.name,
                    'genre':  artist.genre.name,
                'popularity': artist.total_play_count,
                    'album':  [
                            {'name':        album.name,
                            'imgUrl':       album.image_url,
                            'country':      album.country.name,
                            'type':         album.album_type.name,
                        }for album in artist.album_set.all()],
                'music': [
                    {'name':        music.name,
                    'streamingUrl': music.streaming_url,
                    }for music in artist.music_set.all()],

            }for artist in artists
        ]

        self.assertEqual(response.json(), {'aritst': artist_info})
        self.assertEqual(response.status_code, 200)

class ArtistIDTest(TestCase):
    maxDiff = None

    def setUp(self):
        client = Client()
        AlbumType.objects.create(
            id=1,
            name='정규',
        )
        Gender.objects.create(
            id=1,
            name='Male',
        )
        Genre.objects.create(
            id=1,
            name='국내 발라드',
        )
        Country.objects.create(id=1, name='Korea')
        ArtistType.objects.create(id=1, name='솔로')
        Artist.objects.create(
            id=1,
            name='김동률',
            artist_type=ArtistType.objects.get(id=1),
            gender=Gender.objects.get(id=1),
            profile_image_url='https://dimg.donga.com/wps/NEWS/IMAGE/2019/12/02/98619588.1.jpg',
            genre = Genre.objects.get(id=1))
        Album.objects.create(
            id=1,
            name='김동률과 아재들',
            artist=Artist.objects.get(id=1),
            release_date='2009-01-23',
            album_type=AlbumType.objects.get(id=1),
            image_url='https://unsplash.com/photos/pvzlggtEr3U',
            country=Country.objects.get(id=1)
        )
        AlbumGenre.objects.create(id=1,
        album=Album.objects.get(id=1),
        genre=Genre.objects.get(id=1))
        Music.objects.create(
            id=1,
            name='우리가 살아가는 이유',
            streaming_url='https://unsplash.com/photos/pvzlggtEr3U',
            album=Album.objects.get(id=1),
            artist=Artist.objects.get(id=1))
        MusicDetail.objects.create(music=Music.objects.get(id=1),
        lyric='배고프다 하지마',
        play_count='93991')

    def tearDown(self):
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
        MusicDetail.objects.all().delete()

    def test_artistid_get_success(self):
        client = Client()
        response = self.client.get('/music/artist/1')
        artist_id=1
        artists     = Artist.objects.filter(id=artist_id).select_related('artist_type','gender','genre').prefetch_related('album_set','music_set', 'music_set__musicdetail').                annotate(total_play_count=Sum('music__musicdetail__play_count'))

        artist_info = [
                {
                    'artist':        artist.name,
                    'imgUrl':  artist.profile_image_url,
                    'type':   artist.artist_type.name,
                    'gender': artist.gender.name,
                    'genre':  artist.genre.name,
                    'popularity' : artist.total_play_count,

                    'album':         [
                        {'name':         album.name,
                            'image':         album.image_url,
                        'country':      album.country.name,
                        'type':         album.album_type.name,
                            }for album in artist.album_set.all()],

                  'music': [
                         { 'name':         music.name,
                         'streaming_url': music.streaming_url,
                         }for music in artist.music_set.all()],

            }for artist in artists
        ]

        self.assertEqual(response.json(), {'aritst': artist_info})
        self.assertEqual(response.status_code, 200)

class AlbumInfoTest(TestCase):
    maxDiff = None

    def setUp(self):
        client = Client()
        AlbumType.objects.create(
            id=1,
            name='정규',
        )
        Gender.objects.create(
            id=1,
            name='Male',
        )
        Genre.objects.create(
            id=1,
            name='국내 발라드',
        )
        Country.objects.create(id=1, name='Korea')
        ArtistType.objects.create(id=1, name='솔로')
        Artist.objects.create(
            id=1,
            name='김동률',
            artist_type=ArtistType.objects.get(id=1),
            gender=Gender.objects.get(id=1),
            profile_image_url='https://dimg.donga.com/wps/NEWS/IMAGE/2019/12/02/98619588.1.jpg',
            genre = Genre.objects.get(id=1))
        Album.objects.create(
            id=1,
            name='김동률과 아재들',
            artist=Artist.objects.get(id=1),
            release_date='2009-01-23',
            album_type=AlbumType.objects.get(id=1),
            image_url='https://unsplash.com/photos/pvzlggtEr3U',
            country=Country.objects.get(id=1)
        )
        AlbumGenre.objects.create(id=1,
        album=Album.objects.get(id=1),
        genre=Genre.objects.get(id=1))
        Music.objects.create(
            id=1,
            name='우리가 살아가는 이유',
            streaming_url='https://unsplash.com/photos/pvzlggtEr3U',
            album=Album.objects.get(id=1),
            artist=Artist.objects.get(id=1))
        MusicDetail.objects.create(music=Music.objects.get(id=1),
        lyric='배고프다 하지마',
        play_count='93991')

    def tearDown(self):
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
        MusicDetail.objects.all().delete()

    def test_albuminfo_get_success(self):
        client = Client()
        response = self.client.get('/music/album/info')
        albums = Album.objects.select_related('album_type','country').prefetch_related('genre','emotion','mood','artist','music_set', 'music_set__musicdetail').annotate(total_album_play_count=Sum('music__musicdetail__play_count'))
        album_info =[
            {
                'album_id':     album.id,
                'album_name':   album.name,
                'popularity':   album.total_album_play_count,
                'country':      album.country.name,
                'artist_name':  album.artist.name,
                'artist_type':  album.artist.artist_type.name,
                'album_genre':  album.albumgenre_set.get().genre.name,
                'album_type':   album.album_type.name,
                'album_cover':  album.image_url,
                'track_info': [
                    {
                            'id': music.id,
                            'name': music.name,
                        'streaming_url': music.streaming_url,
                        }for music in album.music_set.all()],
            }for album in albums
        ]

        self.assertEqual(response.json(), {'albums': album_info})
        self.assertEqual(response.status_code, 200)

class AlbumIDTest(TestCase):
    maxDiff = None

    def setUp(self):
        client = Client()
        AlbumType.objects.create(
            id=1,
            name='정규',
        )
        Gender.objects.create(
            id=1,
            name='Male',
        )
        Genre.objects.create(
            id=1,
            name='국내발라드',
        )
        Country.objects.create(id=1, name='Korea')
        ArtistType.objects.create(id=1, name='솔로')
        Artist.objects.create(
            id=1,
            name='김동률',
            artist_type=ArtistType.objects.get(id=1),
            gender=Gender.objects.get(id=1),
            profile_image_url='https://dimg.donga.com/wps/NEWS/IMAGE/2019/12/02/98619588.1.jpg',
            genre = Genre.objects.get(id=1))
        Album.objects.create(
            id=1,
            name='김동률과 아재들',
            artist=Artist.objects.get(id=1),
            release_date='2009-01-23',
            album_type=AlbumType.objects.get(id=1),
            image_url='https://unsplash.com/photos/pvzlggtEr3U',
            country=Country.objects.get(id=1)
        )
        AlbumGenre.objects.create(id=1,
        album=Album.objects.get(id=1),
        genre=Genre.objects.get(id=1))
        Music.objects.create(
            id=1,
            name='우리가 살아가는 이유',
            streaming_url='https://unsplash.com/photos/pvzlggtEr3U',
            album=Album.objects.get(id=1),
            artist=Artist.objects.get(id=1))
        MusicDetail.objects.create(music=Music.objects.get(id=1),
        lyric='배고프다 하지마',
        play_count='93991')

    def tearDown(self):
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
        MusicDetail.objects.all().delete()

    def test_albumid_get_success(self):
        client = Client()
        response = self.client.get('/music/album/1')
        album_id=1

        album = Album.objects.select_related('album_type','country').prefetch_related('artist','music_set','music_set__musicdetail').                                                        annotate(total_album_play_count=Sum('music__musicdetail__play_count')).get(id=album_id)
        album_info = {
                'album_id':        album.id,
                'album_name':      album.name,
                'album_popularity': album.total_album_play_count,
                 'country':         album.country.name,
                 'artist_name':     album.artist.name,
                 'artist_type':     album.artist.artist_type.name,
                 'album_genre':     album.albumgenre_set.get().genre.name,
                 'release_date':    album.release_date,
                 'album_type':      album.album_type.name,
                 'album_cover':     album.image_url,
                 'release_date':    album.release_date,
                 'track_info': [
                    {       'id'       : music.id,
                             'name'     : music.name,
                         'streaming_url': music.streaming_url,
                         }for music in album.music_set.all()],
            }

        self.assertEqual(response.json(), {'albums': album_info})
        self.assertEqual(response.status_code, 200)
