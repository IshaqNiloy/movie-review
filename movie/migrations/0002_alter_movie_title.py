# Generated by Django 4.2.1 on 2023-07-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]