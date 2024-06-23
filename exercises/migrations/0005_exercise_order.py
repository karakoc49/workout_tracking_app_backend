# Generated by Django 5.0.6 on 2024-05-14 18:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_remove_exercise_video_url_exercise_gif_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='order',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
