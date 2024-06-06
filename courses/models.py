from django.db import models
from django.conf import settings


class Course(models.Model):
    title = models.CharField(max_length=255, help_text="Введите название вашего курса")
    description = models.TextField(help_text="Введите описание вашего курса")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="courses")

    def __str__(self):
        return self.title


