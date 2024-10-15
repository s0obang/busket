from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20)
    userImage=models.ImageField(blank=True, upload_to="image/", default='default.jpeg') #default.jpeg 임시
    
    def __str__(self):
        return self.nickname
    
# Create your models here.
