from django.contrib import admin
from .models import Course, Category
from django.contrib.auth import settings


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)