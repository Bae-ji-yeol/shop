from django.db import models
from django.db.models import Model
from product.models import Game


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    check = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.game.price * self.quantity

    def __str__(self):
        return self.game
