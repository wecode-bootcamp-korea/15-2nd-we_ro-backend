from django.db    import models

from music.models import Genre, Artist, Chart


class User(models.Model):
    email         = models.EmailField()
    password      = models.CharField(max_length=250)
    date_of_birth = models.DateField(null=True)
    phone_number  = models.CharField(max_length=20, null=True)
    kakao_id      = models.IntegerField(null=True)

    class Meta:
        db_table = 'users'


class Character(models.Model):
    name              = models.CharField(max_length=20)
    user              = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image_url = models.URLField(max_length=2000)
    genre             = models.ManyToManyField(Genre, through='CharacterTasteGenre')
    chart             = models.ManyToManyField(Chart, through='CharacterTasteChart')
    artist            = models.ManyToManyField(Artist, through='CharacterTasteArtist')

    class Meta:
        db_table = 'characters'


class CharacterTasteGenre(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    genre     = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'character_taste_genres'


class CharacterTasteChart(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    chart     = models.ForeignKey(Chart, on_delete = models.CASCADE)

    class Meta:
        db_table = 'character_taste_charts'


class CharacterTasteArtist(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    artist    = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        db_table = 'character_taste_artists'

