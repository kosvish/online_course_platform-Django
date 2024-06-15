from django.contrib import admin
from django.urls import path, include
from courses.views import index
from django.contrib.auth import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls', namespace='courses')),
    path('users/', include('users.urls', namespace='users')),
    path('', index, name='main')
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
