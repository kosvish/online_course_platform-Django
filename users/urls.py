from django.urls import path
from .views import registration, login, profile

app_name = 'users'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile')
]
