
from django.urls import path
from .views import home,landing

app_name='home'

urlpatterns = [
    path('', home, name='home'),
    path('landing/', landing, name='landing'),
]