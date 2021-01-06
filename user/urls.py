from django.urls import path

from user.views  import SignUpView, SignInView, TasteArtistView, TasteChartView, TasteGenreView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/taste/artist', TasteArtistView.as_view()),
    path('/taste/chart', TasteChartView.as_view()),
    path('/taste/genre', TasteGenreView.as_view()),
]

