from django.db import models

# Create your models here.
class Post(models.Model):
  nickname = models.CharField(max_length=15)
  title = models.CharField(max_length=50)
  content = models.TextField()
  password = models.CharField(max_length=20)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title