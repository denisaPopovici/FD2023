from django.db import models


# Create your models here.
class Student(models.Model):
    objects = models.Manager()
    code = models.IntegerField(default=1234, blank=False, null=False)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
