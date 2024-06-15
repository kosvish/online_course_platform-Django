from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255, help_text="Введите название вашего курса")
    description = models.TextField(help_text="Введите описание вашего курса")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="instructed_courses")
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="courses")
    image = models.ImageField(upload_to='course_images', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='courses')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:course-detail', args=[str(self.id)])




