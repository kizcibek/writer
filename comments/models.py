from datetime import datetime

from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.db.models import DateTimeField

from main.models import User


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())


class Comments:
    pass