from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    elo_score = models.IntegerField(null=True, default=0)
    angles_score = models.IntegerField(null=True, default=0)
    supports_score = models.IntegerField(null=True, default=0)
    role = models.IntegerField(null=True, default=0)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
