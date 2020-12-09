from django.db import models


class Patient(models.Model):
    """
    creates new users.
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

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
    Feed backs messages from the patients.
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name + ' ' + self.last_name