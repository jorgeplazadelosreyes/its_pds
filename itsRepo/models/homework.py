from django.db import models


class Homework(models.Model):
    diagram = models.JSONField()
    title = models.CharField(max_length=20)
    difficulty = models.IntegerField(null=True)