# Generated by Django 5.0.7 on 2024-07-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funfacts', '0003_alter_song_video_remove_song_cat_song_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='cat',
            field=models.ManyToManyField(related_name='categories', to='funfacts.category'),
        ),
    ]
