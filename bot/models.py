from django.db import models


class Item(models.Model):
    cid = models.CharField(max_length=25)
    dumb = models.IntegerField(default=0)
    stupid = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
