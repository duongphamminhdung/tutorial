from django.db import models

# Create your models here.
class Members(models.Model):
    title = models.CharField(max_length=255)
    hs11 = models.CharField(max_length=255)
    hs12 = models.CharField(max_length=255)
    hs13 = models.CharField(max_length=255)
    hs14 = models.CharField(max_length=255)
    GK = models.CharField(max_length=255)
    CK = models.CharField(max_length=255)
    GOAL = models.CharField(max_length=255)