from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

class EmailSub(models.Model):
    name = CharField(max_length=100)
    email = EmailField(max_length=200)

class ServiceRequest(models.Model):
    first_name = CharField()
    last_name = CharField()
    email = EmailField()
    phone = CharField()
    service = CharField()
    message = TextField()