from django.urls import path
from .views import signup, login, notloginmy, logout, my

app_name='accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('my/notlogin', notloginmy, name='notloginmy'),
    path('my/<int:user_id>', my, name='my'),
]
