# Generated by Django 3.0.2 on 2020-02-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='img',
            field=models.ImageField(blank=True, upload_to='photos/recipe'),
        ),
    ]