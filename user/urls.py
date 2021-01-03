from django.urls import path

from user.views  import CharacterCreateView, CharacterNameChangeView


urlpatterns = [
    path('/<int:user_id>/character/create', CharacterCreateView.as_view()),
    path('/<int:user_id>/character/<int:character_id>', CharacterNameChangeView.as_view()),
]
