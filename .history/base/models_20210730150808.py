from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    # thumbnail = models.ImageField()
    body = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(a)