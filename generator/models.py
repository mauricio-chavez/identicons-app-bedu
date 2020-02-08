"""Generator app models"""

from django.contrib.auth.models import User
from django.db import models


class Identicon(models.Model):
    """Identicon model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='identicons')
    created_at = models.DateTimeField(auto_now=True)


class RandomWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now=True)
