from django.db import models
from django.conf import settings


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    