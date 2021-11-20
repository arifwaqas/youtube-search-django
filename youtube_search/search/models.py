from django.db import models

class ResultModel(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=100)
    pubdate=models.CharField(max_length=1000)
    thumb=models.CharField(max_length=1000)

