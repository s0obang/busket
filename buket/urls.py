
from django.urls import path
from .views import buket, buy, share

app_name='buket'

urlpatterns = [
    path('', buket, name='buket'),
    path('share/', share, name='share'),
    path('buy/', buy, name='buy'),
]