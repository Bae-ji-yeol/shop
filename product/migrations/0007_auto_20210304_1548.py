# Generated by Django 3.1.7 on 2021-03-04 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210304_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='main_image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='thumbnail_image',
        ),
        migrations.AddField(
            model_name='game',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='main_image/'),
        ),
        migrations.AddField(
            model_name='game',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail_image/'),
        ),
    ]
