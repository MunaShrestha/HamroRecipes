# Generated by Django 3.0.2 on 2020-02-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0003_auto_20200212_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='incredient1',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient10',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient11',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient12',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient13',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient14',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient15',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient16',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient17',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient2',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient3',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient4',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient5',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient6',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient7',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient8',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='incredient9',
        ),
        migrations.AddField(
            model_name='recipe',
            name='incredients',
            field=models.TextField(default=1),
        ),
    ]
