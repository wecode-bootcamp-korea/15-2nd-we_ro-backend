from django.urls import path

from user.views  import CharacterCreateView


urlpatterns = [
    path('/<int:user_id>/character/create', CharacterCreateView.as_view()),
]
