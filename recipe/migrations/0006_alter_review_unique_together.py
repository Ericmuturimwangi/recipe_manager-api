# Generated by Django 5.1.1 on 2024-10-08 11:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_remove_recipe_is_scheduled_review_schedule_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'recipe')},
        ),
    ]
