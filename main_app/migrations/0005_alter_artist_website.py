# Generated by Django 3.2.4 on 2021-06-18 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_artist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='website',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]