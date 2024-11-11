from django.db import models
from django.conf import settings

# Create your models here.
class Buket(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    busketName=models.CharField(max_length=20)
    busketPrice=models.CharField(max_length=20)
    busketShop = models.CharField(max_length=20)
    busketShopUrl = models.CharField(max_length=20)
    busketCategory = models.CharField(max_length=20)
    userImage=models.ImageField(blank=True, upload_to="buscketImage/", default='default.jpeg')
