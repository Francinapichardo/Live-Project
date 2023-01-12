from django.db import models

# Create your models here.

class Traveling(models.Model):
  First_Name = models.CharField(max_length=255, default="", blank=True, null=False)
  Last_name = models.CharField(max_length=255, default="", blank=True, null=False)
  Email = models.CharField(max_length=255, default="", blank=True, null=False)
  Phone_Number = models.CharField(max_length=255, blank=True, null=False)

  objects = models.Manager()

  def __str__(self):
    return self.First_Name
