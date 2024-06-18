from django.contrib import admin
from django.urls import path, include
from courses.views import index
from django.contrib.auth import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .swagger import BothHttpAndHttpsSchemaGenerator
import json


schema_view = get_schema_view(
    openapi.Info(
        title='Email-verify API',
        default_version='v1',
        description='API, который позволит пользователям отправлять регистрацию, и API будет проверять '
                    'электронные письма',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email="mr.kocta@bk.ru"),
        license=openapi.License(name='BSD License')
    ),
    permission_classes=[permissions.AllowAny]
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls', namespace='courses')),
    path('users/', include('users.urls', namespace='users')),
    path('', index, name='main'),
    path('openapi/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
