from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField()
    #auto_now set the date value to current date time
    #auto_now_add set the date value to when the post is created
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
