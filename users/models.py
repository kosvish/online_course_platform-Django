from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group, related_name='custom_user_set',
        blank=True,
        help_text='Группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения '
                  'предоставленной каждой из их групп.',
        related_query_name = 'custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permission_set',
        blank=True,
        help_text='Особые разрешения для этого пользователя',
        related_query_name='custom_user_permission'
    )
    image = models.ImageField(upload_to="user_images", blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone_number = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return ({
            'refresh': str(refresh),
            'refresh': str(refresh.access_token),
        })


