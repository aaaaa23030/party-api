# Generated by Django 5.1.3 on 2024-11-30 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happy_new_party_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='members',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
