from django.db import models


class Student(models.Model):
    eloScore = models.IntegerField(null=True)
    anglesForce = models.IntegerField(null=True)
    supportsForce = models.IntegerField(null=True)
