from django.db    import models

from user.models  import Character
from music.models import Music, Album, Artist


class Mylist(models.Model):
    name       = models.CharField(max_length=45)
    character  = models.ForeignKey(Character, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    music      = models.ManyToManyField(Music, through = 'MyListMusic')

    class Meta:
        db_table = 'mylists'


class MylistMusic(models.Model):
    mylist = models.ForeignKey(Mylist, on_delete=models.CASCADE)
    music  = models.ForeignKey(Music, on_delete=models.CASCADE)

    class Meta:
        db_table = 'mylist_musics'


class StorageMusic(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    music     = models.ForeignKey(Music, on_delete=models.CASCADE)

    class Meta:
        db_table = 'storage_musics'


class StorageAlbum(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    album     = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        db_table = 'storage_albums'


class StorageArtist(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    artist    = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        db_table = 'storage_artists'

