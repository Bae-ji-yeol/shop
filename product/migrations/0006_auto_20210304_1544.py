# Generated by Django 3.1.7 on 2021-03-04 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210304_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='sub_image',
            field=models.ImageField(blank=True, null=True, upload_to='sub_image/'),
        ),
    ]
