import json, datetime

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ObjectDoesNotExist
from django.db.models       import Prefetch, Sum

from .models import (
    AlbumType,
    Country,
    ArtistType,
    Gender,
    Genre,
    Emotion,
    Mood,
    Chart,
    Artist,
    Album,
    AlbumGenre,
    Music,
    MusicDetail,
    AlbumEmotion,
    AlbumChart)

class MusicsView(View):
    def get(self, request):
        LIMIT      = 70
        OFFSET     = 0

        musics     = Music.objects.select_related('album', 'album__country', 'artist', 'artist__genre').order_by('id')
        music_info = [
                {
                    'rank'         :    music.id,
                    'title'        :    music.name,
                    'country'      :    music.album.country.name,
                    'imgUrl'       :    music.album.image_url,
                    'album'        :    music.album.name,
                    'artist'       :    music.artist.name,
                    'genre'        :    music.artist.genre.name,
        } for music in musics [OFFSET:OFFSET+LIMIT]]
        return JsonResponse({'MusicInfo': music_info}, status=200)


class CountryMusicView(View):
    def get(self, request, country_id):
        try:
            LIMIT = 50
            OFFSET = 0
            musics = Music.objects.filter(album__country_id = country_id).select_related('album__country', 'album', 'artist', 'artist__genre').prefetch_related('album__genre', 'musicdetail').order_by('id')

            music_info=[
                {
                    'rank'         :    music.id,
                    'title'        :    music.name,
                    'country'      :    music.album.country.name,
                    'imgUrl'       :    music.album.image_url,
                    'album'        :    music.album.name,
                    'artist'       :    music.artist.name,
                    'genre'        :    music.artist.genre.name,
                }for music in musics[OFFSET:OFFSET+LIMIT]]
            return JsonResponse({'Music_info': music_info}, status=200)
        except Country.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'COUNTRY_ID_NOT_FOUND'}, status=404)

class MusicIDView(View):
    def get(self, request, music_id):
        try:
            music = Music.objects.prefetch_related('musicdetail', 'album__albumgenre_set__genre').select_related('album', 'artist').get(id=music_id)

            music_info ={
                'id'        :  music.id,
                'title'     :  music.name,
                'url'       :  music.streaming_url,
                'imgUrl'    :  music.album.image_url,
                'album'     :  music.album.name,
                'genre'     :  music.artist.genre.name,
                'artist'    :  music.artist.name,
                'rated_r'   :  music.musicdetail.is_rated_r,
                'popularity':  music.musicdetail.play_count,
            }
            return JsonResponse({'Music_info': music_info}, status=200)
        except Music.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'MUSIC_ID_NOT_FOUND'}, status=404)

class ArtistsView(View):
    def get(self, request):
        artists = Artist.objects.select_related('artist_type','gender','genre').prefetch_related('album_set','music_set','music_set__musicdetail').annotate(total_play_count=Sum('music__musicdetail__play_count'))

        artist_info = [
            {
                    'name'   :  artist.name,
                    'image'  :  artist.profile_image_url,
                    'genre'  :  artist.genre.name,
                'popularity' :  artist.total_play_count,
            }for artist in artists
        ]

        return JsonResponse({'artist': artist_info}, status=200)

class ArtistIDView(View):
    def get(self,requst, artist_id):
        try:
            artists     = Artist.objects.filter(id=artist_id).select_related('artist_type','gender','genre').prefetch_related('album_set','music_set', 'music_set__musicdetail').annotate(total_play_count=Sum('music__musicdetail__play_count'))

            artist_info = [
                {
                    'artist'    :  artist.name,
                    'imgUrl'    :  artist.profile_image_url,
                    'type'      :  artist.artist_type.name,
                    'gender'    :  artist.gender.name,
                    'genre'     :  artist.genre.name,
                    'popularity':  artist.total_play_count,

                    'album':[
                        {
                        'name'        :   album.name,
                        'image'       :   album.image_url,
                        'release_date':   album.release_date,
                        'country'     :   album.country.name,
                        'type'        :   album.album_type.name,
                            }for album in artist.album_set.all()],

                 'music': [
                        {
                            'name'     : music.name,
                        'streaming_url': music.streaming_url,
                        }for music in artist.music_set.all()],

             }for artist in artists
        ]
            return JsonResponse({'aritst': artist_info}, status=200)
        except Artist.DoesNotExist:
            JsonResponse({'MESSAGE' : 'MUSIC_ID_NOT_FOUND'}, status=404)


class AlbumsView(View):
    def get(self, request):

        LIMIT   = 50
        OFFSET  = 0

        sort     = request.GET.get('sort', None)
        ordering = request.GET.get('ordering', None)
        albums   = Album.objects.prefetch_related('artist','artist__genre', 'music_set',  'music_set__musicdetail')

        album_info =[
            {
                'album_id'     :   album.id,
                'album_name'   :   album.name,
                'artist_name'  :   album.artist.name,
                'album_genre'  :   album.artist.genre.name,
                'album_cover'  :   album.image_url,
                'track_info': [
                    {
                            'id'       :  music.id,
                            'name'     :  music.name,
                        }for music in album.music_set.all()],
            }for album in albums[OFFSET:OFFSET+LIMIT]]
        return JsonResponse({'albums': album_info}, status=200)

class AlbumIDView(View):
    def get(self, request, album_id):
        try:
            album = Album.objects.select_related('album_type','country').prefetch_related('artist','music_set','music_set__musicdetail').annotate(total_album_play_count=Sum('music__musicdetail__play_count')).get(id=album_id)
            album_info = {
                'album_id'        :    album.id,
                'album_name'      :    album.name,
                'album_popularity':    album.total_album_play_count,
                'country'         :    album.country.name,
                'artist_name'     :    album.artist.name,
                'artist_type'     :    album.artist.artist_type.name,
                'album_genre'     :    album.artist.genre.name,
                'release_date'    :    album.release_date,
                'album_type'      :    album.album_type.name,
                'album_cover'     :    album.image_url,
                'release_date'    :    album.release_date,
                'track_info': [
                    {       'id'       : music.id,
                            'name'     : music.name,
                        'streaming_url': music.streaming_url,
                        }for music in album.music_set.all()],
            }

            return JsonResponse({'album': album_info}, status=200)
        except Album.DoesNotExist:
            JsonResponse({'Message': 'INVADLID_Album_Info'}, status=404)
