# Generated by Django 3.1.2 on 2020-10-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appetizers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(max_length=32),
        ),
    ]
