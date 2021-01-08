from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('profile_image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'characters',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=250)),
                ('date_of_birth', models.DateField(null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('kakao_id', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='CharacterTasteGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.character')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.genre')),
            ],
            options={
                'db_table': 'character_taste_genres',
            },
        ),
        migrations.CreateModel(
            name='CharacterTasteChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.character')),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.chart')),
            ],
            options={
                'db_table': 'character_taste_charts',
            },
        ),
        migrations.CreateModel(
            name='CharacterTasteArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.character')),
            ],
            options={
                'db_table': 'character_taste_artists',
            },
        ),
        migrations.AddField(
            model_name='character',
            name='artist',
            field=models.ManyToManyField(through='user.CharacterTasteArtist', to='music.Artist'),
        ),
        migrations.AddField(
            model_name='character',
            name='chart',
            field=models.ManyToManyField(through='user.CharacterTasteChart', to='music.Chart'),
        ),
        migrations.AddField(
            model_name='character',
            name='genre',
            field=models.ManyToManyField(through='user.CharacterTasteGenre', to='music.Genre'),
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
