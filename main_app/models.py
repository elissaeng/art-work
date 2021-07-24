from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User 
# Create your models here.

# GALLERY
class Gallery(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  blurb = models.CharField(max_length=100, blank=True )
  bio = models.TextField(max_length=350)
  profile_img = models.CharField(max_length=200, blank=True)
  highlights = models.TextField(max_length=200)
  fun_fact = models.TextField(max_length=150)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  website = models.CharField(max_length=50, blank=True)
  artists = models.ManyToManyField('Artist', blank=True )

  def _str_(self):
    return f'{self.name}'

# ARTIST
class Artist(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  blurb = models.CharField(max_length=100, blank=True)
  bio = models.TextField(max_length=350)
  profile_img = models.CharField(max_length=200, blank=True)
  highlights = models.TextField(max_length=200)
  fun_fact = models.TextField(max_length=150)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  website = models.CharField(max_length=50, blank=True)
  galleries = models.ManyToManyField(Gallery, blank=True)

  def _str_(self):
    return f'{self.name}'

# ARTIST PHOTOS
class Artist_photo(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  url = models.CharField(max_length=200)
  # image = models.ImageField(upload_to='uploads/', height_field=200, width_field=200)

  def __str__(self):
    return f"Photo for artist_id: {self.artist_id} @{self.url}"



# GALLERY PHOTOS
class Gallery_photo(models.Model):
  gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)    
  url = models.CharField(max_length=200)