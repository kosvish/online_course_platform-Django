from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


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


