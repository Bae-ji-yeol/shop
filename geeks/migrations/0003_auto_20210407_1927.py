# Generated by Django 3.1.7 on 2021-04-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0002_auto_20210406_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeksmodel',
            name='geeks_field',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
