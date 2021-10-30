from django.db import models

# Create your models here.

class Gainer(models.Model):
    symbol = models.CharField(max_length=20)
    open_price = models.DecimalField(max_digits=8, decimal_places=2)
    high_price = models.DecimalField(max_digits=8, decimal_places=2)
    low_price = models.DecimalField(max_digits=8, decimal_places=2)
    prev_price = models.DecimalField(max_digits=8, decimal_places=2)
    net_price = models.DecimalField(max_digits=8, decimal_places=2)
    turnover = models.DecimalField(max_digits=10, decimal_places=2)
    trade_quantity = models.IntegerField()
    ltp = models.DecimalField(max_digits=8, decimal_places=2)
    perChange = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.symbol

class Test(models.Model):
    name = models.CharField(max_length=4)