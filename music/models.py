from django.db   import models

class AlbumType(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'album_types'


class Country(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'countries'


class ArtistType(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'artist_types'


class Gender(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'genders'


class Genre(models.Model):
    name = models.CharField(max_length =10)

    class Meta:
        db_table = 'genres'


class Emotion(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'emotions'


class Mood(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'moods'


class Chart(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'charts'

class Artist(models.Model):
    name              = models.CharField(max_length=20)
    artist_type       = models.ForeignKey(ArtistType, on_delete=models.CASCADE)
    gender            = models.ForeignKey(Gender, on_delete=models.CASCADE)
    genre             = models.ForeignKey(Genre, on_delete=models.CASCADE)
    profile_image_url = models.URLField(max_length = 2000, null=True)

    class Meta:
        db_table = 'artists'


class Album(models.Model):
    name         = models.CharField(max_length=45)
    artist       = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    album_type   = models.ForeignKey(AlbumType, on_delete = models.CASCADE)
    image_url    = models.URLField(max_length=2000)
    country      = models.ForeignKey(Country, on_delete = models.CASCADE)
    genre        = models.ManyToManyField(Genre, through='AlbumGenre')
    emotion      = models.ManyToManyField(Emotion, through='AlbumEmotion')
    mood         = models.ManyToManyField(Mood, through='AlbumMood')
    chart        = models.ManyToManyField(Chart, through='AlbumChart')

    class Meta:
        db_table = 'albums'


class AlbumGenre(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'album_genres'


class Music(models.Model):
    name          = models.CharField(max_length=45)
    streaming_url = models.URLField(max_length=2000)
    album         = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist        = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        db_table = 'musics'


class MusicDetail(models.Model):
    music       = models.OneToOneField('Music', on_delete=models.CASCADE)
    lyric       = models.TextField()
    composer    = models.CharField(max_length=10, null=True)
    lyricist    = models.CharField(max_length=10, null=True)
    arrangement = models.CharField(max_length=10, null=True)
    is_rated_r  = models.BooleanField(default=False)
    play_count  = models.IntegerField(default=0)

    class Meta:
        db_table = 'music_details'


class AlbumEmotion(models.Model):
    album   = models.ForeignKey(Album, on_delete=models.CASCADE)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)

    class Meta:
        db_table = 'album_emotions'


class AlbumMood(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    mood  = models.ForeignKey(Mood, on_delete=models.CASCADE)

    class Meta:
        db_table = 'album_moods'


class AlbumChart(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    chart = models.ForeignKey(Chart, on_delete = models.CASCADE)

    class Meta:
        db_table = 'album_charts'


