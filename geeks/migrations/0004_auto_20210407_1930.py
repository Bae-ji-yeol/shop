# Generated by Django 3.1.7 on 2021-04-07 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0003_auto_20210407_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeksmodel',
            name='geeks_field',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]