# Generated by Django 3.1.7 on 2021-03-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210326_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='point',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
