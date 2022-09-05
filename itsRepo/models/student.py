from statistics import mode
from django.db import models


class Student(models.Model):
    eloScore = models.IntegerField()
