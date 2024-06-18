from django.urls import path
from .views import registration, login, profile, SingUp, VerifyEmail

app_name = 'users'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
]

urlpatterns += [
    path('', SingUp.as_view(), name='signup'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify')
]
