# Generated by Django 3.1.7 on 2021-04-02 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20210401_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='cart_item',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='game',
        ),
    ]
