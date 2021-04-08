from django.db import models
from users.models import Account


class Game(models.Model):
    title = models.CharField(max_length=200)
    maker = models.CharField(max_length=50)
    create_date = models.DateField()
    price = models.DecimalField(max_digits=100000, decimal_places=0)
    category = models.CharField(max_length=50)
    stock = models.IntegerField()
    posted_date = models.DateTimeField()
    main_image = models.ImageField(upload_to='main_image/', blank=True, null=True)
    sub1_image = models.ImageField(upload_to='sub1_image/', blank=True, null=True)
    sub2_image = models.ImageField(upload_to='sub2_image/', blank=True, null=True)
    sub3_image = models.ImageField(upload_to='sub3_image/', blank=True, null=True)
    content = models.TextField()
    ds = models.BooleanField(default=False)

    class Meta:
        ordering = ('title', )
        verbose_name = 'game'
        verbose_name_plural = 'games'

    def __str__(self):
        return '{}'.format(self.title)


class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    content = models.TextField()
    posted_date = models.DateTimeField()


class Tag(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    tag = models.CharField(max_length=10)
