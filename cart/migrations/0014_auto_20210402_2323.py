# Generated by Django 3.1.7 on 2021-04-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_auto_20210402_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]