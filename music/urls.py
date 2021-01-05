from django.urls import path
from music.views import AlbumIDView, AlbumsView, MusicsView, MusicIDView, CountryMusicView, ArtistsView, ArtistIDView

urlpatterns = [
    path('/albums', AlbumsView.as_view()),
    path('/album/<int:album_id>', AlbumIDView.as_view()),
    path('/artists', ArtistsView.as_view()),
    path('/artist/<int:artist_id>', ArtistIDView.as_view()),
    path('/country/<int:country_id>', CountryMusicView.as_view()),
    path('', MusicsView.as_view()),
    path('/<int:music_id>', MusicIDView.as_view()),
]

