from django.db import models


# Create your models here.
class Clothes(models.Model):
    name = models.TextField()
    image_url = models.TextField()
    link = models.TextField()


class Advice(models.Model):
    clothes = models.ManyToManyField(Clothes)