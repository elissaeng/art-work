# Generated by Django 3.2.4 on 2021-06-23 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20210623_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.TextField(max_length=350),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='bio',
            field=models.TextField(max_length=350),
        ),
    ]