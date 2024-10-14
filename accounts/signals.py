from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Profile

import random
import string

def random_nickname(length=8):
    while True:
        nickname = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        if not Profile.objects.filter(nickname=nickname).exists(): 
            return nickname


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        nickname = random_nickname()
        Profile.objects.create(user=instance, nickname=nickname)