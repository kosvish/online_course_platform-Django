from django.contrib import admin
from django.urls import path, include
from courses.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls'), name='courses'),
    path('', index, name='main')
]
