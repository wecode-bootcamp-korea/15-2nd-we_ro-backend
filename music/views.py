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

# 음원 전체
# 국가별 / 장르별 / play_count 별
class MusicsView(View):
    def get(self, request):
        limit      = int(request.GET.get("limit",15))
        offset     = int(request.GET.get("offset",0))
        musics     = Music.objects.all()
        music_info = [
                {
                    'rank'         :    music.id,
                    'title'        :    music.name,
                    'country'      :    music.album.country.name,
                    'url'          :    music.streaming_url,
                    'imgUrl'       :    music.album.image_url,
                    'album'        :    music.album.name,
                    'artist'       :    music.artist.name,
                    'rated_r'      :    music.musicdetail.is_rated_r,
                    'popularity'   :    music.musicdetail.play_count,
                    'lyric'        :    music.musicdetail.lyric,
                    'artist_type'  :    music.artist.artist_type.name,
                    'artist_gender':    music.artist.gender.name,
                    'genre'        :    music.artist.genre.name,
                    'emotion'      :    music.album.emotion.name,
                    'mood'         :    music.album.mood.name,
                    'chart'        :    music.album.chart.name,
        } for music in musics [offset:offset+limit]]
        return JsonResponse({'MusicInfo': music_info}, status=200)

# 국가에 따른 음악 차트
class CountryMusicView(View):
    def get(self, request, country_id):
        try:
            limit  = int(request.GET.get("limit",15))
            offset = int(request.GET.get("offset",0))
            musics = Music.objects.filter(id__in = Album.objects.filter(country = country_id)).select_related('album', 'artist', 'musicdetail').order_by('-musicdetail__play_count')

            music_info=[
                {
                    'rank'         :    music.id,
                    'title'        :    music.name,
                    'country'      :    music.album.country.name,
                    'url'          :    music.streaming_url,
                    'imgUrl'       :    music.album.image_url,
                    'album'        :    music.album.name,
                    'artist'       :    music.artist.name,
                    'rated_r'      :    music.musicdetail.is_rated_r,
                    'popularity'   :    music.musicdetail.play_count,
                    'lyric'        :    music.musicdetail.lyric,
                    'artist_type'  :    music.artist.artist_type.name,
                    'artist_gender':    music.artist.gender.name,
                    'genre'        :    music.artist.genre.name,
                    'emotion'      :    music.album.emotion.name,
                    'mood'         :    music.album.mood.name,
                    'chart'        :    music.album.chart.name,
                }for music in musics[offset:offset+limit]]
            return JsonResponse({'Music_info': music_info}, status=200)
        except Country.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'COUNTRY_ID_NOT_FOUND'}, status=404)

class MusicIDView(View):
    def get(self, request, music_id):
        try:
            music = Music.objects.get(id=music_id)

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

# 모든 가수 정보->해결해할 부분: 전체 트랙 재생 숫자 합산/ 필터링 적용
class ArtistsView(View):
    def get(self, request):
        artists = Artist.objects.select_related('artist_type','gender','genre').prefetch_related('album_set','music_set','music_set__musicdetail').annotate(total_play_count=Sum('music__musicdetail__play_count'))

        artist_info = [
            {
                    'name'   :  artist.name,
                    'image'  :  artist.profile_image_url,
                    'type'   :  artist.artist_type.name,
                    'gender' :  artist.gender.name,
                    'genre'  :  artist.genre.name,
                'popularity' :  artist.total_play_count,
                    'album':  [
                            {'name'       : album.name,
                            'imgUrl'      : album.image_url,
                            'release_date': album.release_date,
                            'country'     : album.country.name,
                            'type'        : album.album_type.name,
                        }for album in artist.album_set.all()],
                'music': [
                    {'name'       : music.name,
                    'streamingUrl': music.streaming_url,
                    }for music in artist.music_set.all()],

            }for artist in artists
        ]

        return JsonResponse({'artist': artist_info}, status=200)

# 특정 가수 정보-> musicdetail 로 가서 playcount 합
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

# 전체 앨범

class AlbumsView(View):
    def get(self, request):

        sort     = request.GET.get('sort', None)
        ordering = request.GET.get('ordering', None)
        albums   = Album.objects.select_related('album_type','country').prefetch_related('genre','emotion','mood','artist','music_set',  'music_set__musicdetail').annotate(total_album_play_count=Sum('music__musicdetail__play_count'))

        album_info =[
            {
                'album_id'     :   album.id,
                'album_name'   :   album.name,
                'popularity'   :   album.total_album_play_count,
                'country'      :   album.country.name,
                'artist_name'  :   album.artist.name,
                'artist_type'  :   album.artist.artist_type.name,
                'album_genre'  :   album.artist.genre.name,
                'release_date' :   album.release_date,
                'album_type'   :   album.album_type.name,
                'album_cover'  :   album.image_url,
                'release_date' :   album.release_date,
                'track_info': [
                    {
                            'id'       :  music.id,
                            'name'     :  music.name,
                        'streaming_url': music.streaming_url,
                        }for music in album.music_set.all()],
            }for album in albums[offset:offset+limit]]
        return JsonResponse({'albums': album_info}, status=200)

# 특정 앨범 정보
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
