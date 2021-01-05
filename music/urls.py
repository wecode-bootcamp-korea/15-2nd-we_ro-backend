from django.urls import path
from music.views import AlbumIDView, AlbumInfoView, MusicInfoView,MusicIDView, CountryMusicView, ArtistInfoView, ArtistIDView

urlpatterns = [
    path('/album/info', AlbumInfoView.as_view()),
    path('/album/<int:album_id>', AlbumIDView.as_view()),
    path('/artist/info', ArtistInfoView.as_view()),
    path('/artist/<int:artist_id>', ArtistIDView.as_view()),
    path('/country/<int:country_id>', CountryMusicView.as_view()),
    path('', MusicInfoView.as_view()),
    path('/<int:music_id>', MusicIDView.as_view()),
]

