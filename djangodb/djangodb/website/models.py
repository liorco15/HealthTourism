from django.db import models
import datetime
from django.db import models

# from profiles.models import Profile

# Create your models here.

class Messages(models.Model):
    objects = None
    new_message = models.CharField(max_length=100)

    def __str__(self):
        return self.new_message + ' '

class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(Timestamped):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    objects = None
    date = models.DateTimeField(default=datetime.datetime.now)
    # Passport = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)
    # phone_number = models.CharField(max_length=50)

    class Meta:
        default_related_name = 'events'
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name+' '

class DocumentationPA(Timestamped):


    class Meta:
        default_related_name = 'events'
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name+' '