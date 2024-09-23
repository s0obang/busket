from django.urls import path
from .views import signup, login, my

app_name='accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('my/', my, name='my'),
]