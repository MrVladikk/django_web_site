from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date_published")
    likes = models.PositiveIntegerField(default=0)
    comments = models.TextField(blank=True, default="")

    def __str__(self):
        return self.text[:50]
