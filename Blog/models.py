from django.db import models

# Create your models here.
class Student(models.Model):
    eid = models.IntegerField()