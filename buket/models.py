from django.db import models
from django.conf import settings

# Create your models here.
class Bucket(models.model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL)
    busketName=models.CharField()
    busketPrice=models.CharField()
    busketShop = models.CharField()
    busketShopUrl = models.CharField()
    busketCategory = models.CharField()
