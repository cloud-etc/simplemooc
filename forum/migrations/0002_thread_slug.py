# Generated by Django 2.2.6 on 2019-11-02 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='slug',
            field=models.SlugField(default=5, max_length=100, unique=True, verbose_name='Identificador'),
        ),
    ]
