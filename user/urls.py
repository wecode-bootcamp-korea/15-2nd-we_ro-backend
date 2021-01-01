from django.urls import path

from user.views  import SignUpView, CharacterCreateView


urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/character/create', CharacterCreateView.as_view()),
]
