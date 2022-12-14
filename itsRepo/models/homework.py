from django.db import models


class Homework(models.Model):
    diagram = models.JSONField()
    diagram2 = models.JSONField(null=True, blank=True)
    title = models.CharField(max_length=20)
    statement_text = models.TextField(null=True, blank=True, default="")
    statement_file = models.FileField(null=True, upload_to="media/", blank=True)
    difficulty = models.IntegerField(null=True, default=0)
    Fx = models.CharField(max_length=5000, null=True, blank=True)
    Fy = models.CharField(max_length=5000, null=True, blank=True)
    Fm = models.CharField(max_length=5000, null=True, blank=True)
    initial_stage = models.IntegerField(null=True, default=1)
    final_stage = models.IntegerField(null=True, default=1)