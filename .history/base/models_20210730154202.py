from django.db import models
from 

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    # thumbnail = models.ImageField()
    body = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
