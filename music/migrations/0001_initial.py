from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('release_date', models.DateField()),
                ('image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'albums',
            },
        ),
        migrations.CreateModel(
            name='AlbumType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'album_types',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('profile_image_url', models.URLField(max_length=2000, null=True)),
            ],
            options={
                'db_table': 'artists',
            },
        ),
        migrations.CreateModel(
            name='ArtistType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'artist_types',
            },
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'charts',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'emotions',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'genders',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'moods',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('streaming_url', models.URLField(max_length=2000)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
            ],
            options={
                'db_table': 'musics',
            },
        ),
        migrations.CreateModel(
            name='MusicDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyric', models.TextField()),
                ('composer', models.CharField(max_length=10, null=True)),
                ('lyricist', models.CharField(max_length=10, null=True)),
                ('arrangement', models.CharField(max_length=10, null=True)),
                ('is_rated_r', models.BooleanField(default=False)),
                ('play_count', models.IntegerField(default=0)),
                ('music', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='music.music')),
            ],
            options={
                'db_table': 'music_details',
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artisttype'),
        ),
        migrations.AddField(
            model_name='artist',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.gender'),
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.genre'),
        ),
        migrations.CreateModel(
            name='AlbumMood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.mood')),
            ],
            options={
                'db_table': 'album_moods',
            },
        ),
        migrations.CreateModel(
            name='AlbumGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.genre')),
            ],
            options={
                'db_table': 'album_genres',
            },
        ),
        migrations.CreateModel(
            name='AlbumEmotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('emotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.emotion')),
            ],
            options={
                'db_table': 'album_emotions',
            },
        ),
        migrations.CreateModel(
            name='AlbumChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.chart')),
            ],
            options={
                'db_table': 'album_charts',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='album_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.albumtype'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='chart',
            field=models.ManyToManyField(through='music.AlbumChart', to='music.Chart'),
        ),
        migrations.AddField(
            model_name='album',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.country'),
        ),
        migrations.AddField(
            model_name='album',
            name='emotion',
            field=models.ManyToManyField(through='music.AlbumEmotion', to='music.Emotion'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(through='music.AlbumGenre', to='music.Genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='mood',
            field=models.ManyToManyField(through='music.AlbumMood', to='music.Mood'),
        ),
    ]
