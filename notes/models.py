from datetime import timezone
from django.db import models

class Title(models.Model):
  description = models.CharField(max_length=100)
  date_created = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.description
  
class Note(models.Model):
  description = models.CharField(max_length=200)
  date_created = models.DateTimeField(auto_now=True)
  title = models.ForeignKey(Title,on_delete=models.CASCADE)

  def __str__(self):
    return self.description
  
