from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=15)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    medialPic = models.ImageField()

    def __str__(self):
        return self.ticker
