# Generated by Django 3.1.7 on 2021-04-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_auto_20210327_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='ds',
            field=models.BooleanField(default=False),
        ),
    ]