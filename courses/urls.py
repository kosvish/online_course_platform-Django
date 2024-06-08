from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('all/', CourseListView.as_view(), name='course-all')
]
