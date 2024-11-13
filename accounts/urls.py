from django.urls import path
from .views import signup, login, my, logout, my_update

app_name='accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('my/<int:user_id>', my, name='my'),
    path('my/<int:user_id>/update', my_update, name='my_update')
]
