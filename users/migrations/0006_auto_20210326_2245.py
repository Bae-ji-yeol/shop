# Generated by Django 3.1.7 on 2021-03-26 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_account_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='point',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
