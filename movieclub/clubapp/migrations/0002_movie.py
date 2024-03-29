# Generated by Django 5.0.1 on 2024-02-12 16:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(unique=True)),
                ('movie_title', models.CharField(max_length=255)),
                ('added_by_users', models.ManyToManyField(related_name='movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
