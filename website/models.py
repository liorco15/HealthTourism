from django.db import models
import datetime

class Documentation(models.Model):
    objects = None
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    reason_why = models.CharField(max_length=250)
    meeting = models.CharField(max_length=250)
    diagnosis = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Patient(models.Model):
    """
    creates new users.
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    objects = models.Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class SignUp(models.Model):
    """
    contact form / sign up
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    reason_for_referral = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Feedback(models.Model):
    """
    Feedback messages from the patients.
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


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
        return self.name + ' '


class Messages(models.Model):
    objects = None
    new_message = models.CharField(max_length=100)

    def __str__(self):
        return self.new_message + ' '
