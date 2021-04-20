from django.db import models

class TableName(models.Model):
    name =  models.CharField(max_length=100)
    address = models.CharField(max_length=500)