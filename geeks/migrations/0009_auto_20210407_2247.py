# Generated by Django 3.1.7 on 2021-04-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0008_auto_20210407_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeksmodel',
            name='geeks_field',
            field=models.BooleanField(default=False),
        ),
    ]