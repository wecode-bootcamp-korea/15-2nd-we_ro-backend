from django.urls import path


from user.views  import SignUpView, SignInView, CharacterView


urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/character', CharacterView.as_view()),
    path('/character/<int:character_id>', CharacterView.as_view()),
]

