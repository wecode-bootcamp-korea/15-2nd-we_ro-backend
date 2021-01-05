from django.urls import path

from storage.views import MylistView, MylistMusicView

urlpatterns =[
    path('/mylist', MylistView.as_view()),
    path('/mylist/<int:mylist_id>', MylistView.as_view()),
    path('/mylist/<int:mylist_id>/music', MylistMusicView.as_view()),
]
