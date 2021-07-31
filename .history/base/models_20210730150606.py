from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField()
    thumbnail
    body
    slug
    created