from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
