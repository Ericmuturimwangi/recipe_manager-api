# Generated by Django 5.1.1 on 2024-10-07 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_scheduled',
            field=models.BooleanField(default=False),
        ),
    ]
