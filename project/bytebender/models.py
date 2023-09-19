from django.db import models


class registration(models.Model):
     firstname = models.CharField(max_length=50)
     lastname = models.CharField(max_length=50)
     password = models.CharField(max_length=255)
     gender = models.CharField(max_length=50)
     sport = models.CharField(max_length=50)
     email = models.CharField(max_length=40)

class login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
class feedback(models.Model):
    userfeedback = models.CharField(max_length=255)
    username = models.CharField(max_length=50)