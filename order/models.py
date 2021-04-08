from django.db import models


class GameOrder(models.Model):
    user = models.ForeignKey('users.Account', verbose_name="사용자", on_delete=models.CASCADE)
    game = models.ForeignKey('product.Game', verbose_name="게임", on_delete=models.CASCADE)
    cart_item = models.ForeignKey('cart.CartItem', verbose_name='장바구니', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=100000, decimal_places=0, verbose_name='GameOrder total')
    created = models.DateTimeField(auto_now_add=True, verbose_name="구매 시간")
    emailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')

    class Meta:
        db_table = 'Game_Order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)


class GameOrderItem(models.Model):
    game = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=100000, decimal_places=0, verbose_name='GameOrder price')
    order = models.ForeignKey(GameOrder, on_delete=models.CASCADE)

    class Meta:
        db_table = 'GameOrderItem'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.game

