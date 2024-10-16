# Generated by Django 5.1.2 on 2024-10-11 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0004_alter_sound_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sound',
            name='url',
            field=models.URLField(unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='sound',
            name='yt_id',
            field=models.CharField(max_length=50, unique=True, verbose_name='youtube ID'),
        ),
    ]
