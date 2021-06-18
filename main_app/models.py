from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User 
# Create your models here.

# ARTIST
class Artist(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  bio = models.TextField(max_length=300)
  img_urls = models.CharField(max_length=150)
  highlights = models.TextField(max_length=200)
  fun_fact = models.TextField(max_length=150)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  website = models.CharField(max_length=50, blank=True)

  def _str_(self):
    return f'{self.name}'


# PHOTOS
  # class Photo(models.Model):
  #   artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

# GALLERY
class Gallery(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  bio = models.TextField(max_length=300)
  img_urls = models.CharField(max_length=150)
  highlights = models.TextField(max_length=200)
  fun_fact = models.TextField(max_length=150)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  website = models.CharField(max_length=50)

  def _str_(self):
    return f'{self.name}'