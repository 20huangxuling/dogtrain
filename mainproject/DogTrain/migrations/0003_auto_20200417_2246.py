# Generated by Django 3.0.5 on 2020-04-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DogTrain', '0002_auto_20200417_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='img'),
        ),
    ]
