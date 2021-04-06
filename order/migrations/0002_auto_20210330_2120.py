# Generated by Django 3.1.7 on 2021-03-30 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_cartitem_user'),
        ('product', '0022_auto_20210327_1934'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=0, max_digits=100000, verbose_name='GameOrder total')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='구매 시간')),
                ('emailAddress', models.EmailField(blank=True, max_length=250, verbose_name='Email Address')),
                ('cart_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartitem', verbose_name='장바구니')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.game', verbose_name='게임')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문',
                'db_table': 'Game_Order',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GameOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=100000, verbose_name='GameOrder price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.gameorder')),
            ],
            options={
                'db_table': 'GameOrderItem',
            },
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]