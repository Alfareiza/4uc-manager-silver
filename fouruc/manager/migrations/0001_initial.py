# Generated by Django 3.2.2 on 2021-09-29 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('url', models.CharField(max_length=100, unique=True)),
                ('token', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
                ('autoShuffle', models.BooleanField()),
                ('updateflow', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='manager.account')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_id', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('isSubPlaylist', models.BooleanField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='manager.account')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('platform', models.CharField(max_length=28)),
                ('lastContactInMinutes', models.IntegerField(null=True)),
                ('group_id', models.IntegerField()),
                ('group_name', models.CharField(max_length=128)),
                ('status_id', models.IntegerField()),
                ('status_name', models.CharField(max_length=128)),
                ('lastLogReceived', models.DateTimeField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='manager.account')),
                ('playlist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='manager.playlist')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_id', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('file', models.CharField(max_length=13)),
                ('durationInSeconds', models.IntegerField()),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='manager.account')),
                ('category', models.ManyToManyField(related_name='medias', to='manager.Category')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medias', to='manager.client')),
                ('playlist', models.ManyToManyField(related_name='medias', to='manager.Playlist')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('player_id', models.IntegerField()),
                ('media_id', models.IntegerField()),
                ('media_type', models.CharField(max_length=2)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='manager.account')),
            ],
            options={
                'ordering': ['date', 'time'],
                'unique_together': {('date', 'time', 'player_id', 'nickname')},
            },
        ),
    ]
