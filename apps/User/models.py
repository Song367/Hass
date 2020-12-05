
from django.db import models

class Users(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    class Meta:
        db_table='Users'

