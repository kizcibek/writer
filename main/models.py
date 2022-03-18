from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import DateTimeField

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55)
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())
    text = models.TextField()

    def __str__(self):
        return self.title
