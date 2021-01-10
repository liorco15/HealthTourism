from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Documentation(models.Model):
    objects = None
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    reason_why = models.CharField(max_length=250)
    meeting = models.CharField(max_length=250)
    diagnosis = models.CharField(max_length=250)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.completed = False
    #     self.mark = 1
    #     self.get_absolute = 1
    #     self.slug = 'ok'
    #     self.id = 1

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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.completed = False
    #     self.mark = 1
    #     self.get_absolute = 1
    #     self.slug = 'ok'
    #     self.id = 1
    #     self.objects = None

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Feedback(models.Model):
    """
    Feedback messages from the patients.
    """
    object = None
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    message = models.CharField(max_length=250)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.completed = False
    #     self.mark = 1
    #     self.get_absolute = 1
    #     self.slug = 'ok'
    #     self.id = 1
    #     self.objects = None

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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.completed = False
    #     self.mark = 1
    #     self.get_absolute = 1
    #     self.slug = 'ok'
    #     self.id = 1

    def __str__(self):
        return self.name + ' '


class Messages(models.Model):
    objects = None
    subject = models.CharField(max_length=20)
    new_message = models.CharField(max_length=100)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.completed = False
    #     self.mark = True
    #     self.get_absolute = 1
    #     self.slug = 'ok'
    #     self.id = 1

    def __str__(self):
        return self.subject + ' ' + self.new_message


class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    passport = models.CharField(max_length=20, blank=True)
    reason_why = models.CharField(max_length=40, default='a', blank=True)
    meeting = models.CharField(max_length=40, default='a', blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Requests(models.Model):
    objects = None
    subject = models.CharField(max_length=20, default='SOME STRING')
    full_name = models.CharField(max_length=20)
    passport_num = models.CharField(max_length=20)
    request = models.CharField(max_length=250)

    def __str__(self):
        return self.subject + ' ' + self.full_name + ' ' + self.passport_num + ' ' + self.request