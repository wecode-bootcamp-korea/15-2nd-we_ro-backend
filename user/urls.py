from django.urls import path

from user.views  import SignUpView, SignInView, KakaoSignUpView, CharacterView, TasteArtistView, TasteChartView, TasteGenreView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/character', CharacterView.as_view()),
    path('/character/<int:character_id>', CharacterView.as_view()),
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/taste/artist', TasteArtistView.as_view()),
    path('/taste/chart', TasteChartView.as_view()),
    path('/taste/genre', TasteGenreView.as_view()),
    path('/kakao-signup', KakaoSignUpView.as_view()),
]


