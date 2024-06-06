from django.contrib import admin
from .models import Course
from django.contrib.auth import settings
from users.models import User


class CourseAdminInline(admin.TabularInline):
    model = User
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor')
    inlines = [CourseAdminInline]
