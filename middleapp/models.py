from django.db import models

# Create your models here.
class signup(models.Model):
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=100, default="")

    mobile = models.BigIntegerField()

    def __str__(self):
        return self.firstname