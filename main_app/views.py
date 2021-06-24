from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import Artist, Gallery, Artist_photo, Gallery_photo
from .forms import ArtistForm, GalleryForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import uuid
import boto3
# Add these "constants" below the imports
S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'art-work'

# HOME
def home(request):
  artists = Artist.objects.all()
  context = { 'artists': artists }
  return render(request, 'home.html', context)
 

# ///////////// ARTISTS //////////////////

# ARTIST INDEX
def artists_index(request):
  artists = Artist.objects.all()
  context = { 'artists': artists }
  return render(request, 'artists/artists_index.html', context)


# ARTIST SHOW
@login_required
def artist_show(request, artist_id):
  artist_profile = Artist.objects.filter(user=request.user)
  is_gallery = True
  if artist_profile.count() > 0: 
    is_gallery = False
  found_artist = Artist.objects.get(id=artist_id)
  artist_form = ArtistForm()
  context= { 'artist': found_artist, 'ArtistForm': artist_form, 'is_gallery': is_gallery }

  return render(request, 'artists/artist_show.html', context)


# CREATE ARTIST
@login_required 
def artist_create(request):
  if request.method == 'GET':
    form = ArtistForm()
    context = {
      'form': form,
    }
    return render(request, 'artists/artist_create.html', context)
  else:
    form = ArtistForm(request.POST)
    if form.is_valid():
      artist = form.save(commit=False)
      artist.user = request.user
      artist.save()
      return redirect('artist_show', artist.id)


# EDIT ARTIST
@login_required 
def artist_edit(request, artist_id):
  artist = Artist.objects.get(id=artist_id)

  if request.method == 'GET':
    form = ArtistForm(instance=artist)
    context = {
    'form': form
  }
    return render(request, 'artists/artist_edit.html', context)
  else:
    form = ArtistForm(request.POST, instance=artist)
    if form.is_valid():
      artist = form.save()
      return redirect('profile')


# DELETE ARTIST
@login_required 
def artist_delete(request, artist_id):
  artist = Artist.objects.get(id=artist_id)
  artist.delete()
  return redirect('artists_index')


# ARTIST PHOTO
@login_required
def artist_photo(request, artist_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Artist_photo(url=url, artist_id=artist_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
  return redirect('profile')


# GALLERY PHOTO
@login_required
def gallery_photo(request, gallery_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Gallery_photo(url=url,gallery_id=gallery_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
  return redirect('profile')



# ///////// GALLERIES  ///////////  

# GALLERY INDEX
def gallery_index(request):
  galleries = Gallery.objects.all()
  context = { 'galleries': galleries }
  return render(request, 'galleries/gallery_index.html', context)


# GALLERY SHOW
def gallery_show(request, gallery_id):
  artist_profile = Artist.objects.filter(user=request.user)
  is_gallery = True
  if artist_profile.count() > 0: 
    is_gallery = False
  found_gallery = Gallery.objects.get(id=gallery_id)
  gallery_form = GalleryForm()
  context= { 'gallery': found_gallery, 'GalleryForm': gallery_form, 'is_gallery': is_gallery }

  return render(request, 'galleries/gallery_show.html', context)        
  

# EDIT GALLERY
@login_required 
def gallery_edit(request, gallery_id):
  gallery = Gallery.objects.get(id = gallery_id)
  if request.method == 'GET':
    form = GalleryForm(instance=gallery)
    context = {
      'form': form,
    }
    return render(request, 'galleries/gallery_edit.html', context)
  else:
    form = GalleryForm(request.POST, instance=gallery)
    if form.is_valid():
      gallery = form.save()
      return redirect('profile')


# DELETE GALLERY
@login_required 
def gallery_delete(request, gallery_id):
  gallery = Gallery.objects.get(id=gallery_id)
  gallery.delete()
  return redirect('gallery_index')


# SIGN UP
def signup(request):
  error_message = ''
  if request.method == 'POST':
    
    form = UserCreationForm(request.POST)
    
    if form.is_valid():
      value=request.POST.get('isGallery')
      user = form.save()
      if value == 'yes':
        gallery = Gallery() 
        gallery.user = user
        gallery.save()

      else: 
        artist = Artist()
        artist.user = user
        artist.save()

      login(request, user)
      return redirect('profile')
    else:
      error_message = 'Invalid sign up - please try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)       


# PROFILE
def profile(request):
  artist_profile = Artist.objects.filter(user=request.user)
  gallery_profile = Gallery.objects.filter(user=request.user)
  # print (artist_profile[0].galleries)
  if (artist_profile.count()>0):
    following = artist_profile[0].galleries.all()
    return render(request, 'profile.html', {'profile': artist_profile[0], 'following': following, 'is_gallery': False})
  else: 
    following = gallery_profile[0].artists.all()
    return render(request, 'profile.html', {'profile': gallery_profile[0], 'following': following, 'is_gallery': True})


# def artist_show(request, artist_id):
#   found_artist = Artist.objects.get(id=artist_id)
#   artist_form = ArtistForm()
#   context= { 'artist': found_artist, 'ArtistForm': artist_form }

#   return render(request, 'artists/artist_show.html', context)

def assoc_artist(request, artist_id):
  gallery_profile = Gallery.objects.get(user=request.user)
  gallery_profile.artists.add(artist_id)
  gallery_profile.save()
  return redirect('profile')

def assoc_gallery(request, gallery_id):
  artist_profile = Artist.objects.get(user=request.user)
  artist_profile.galleries.add(gallery_id)
  artist_profile.save()
  return redirect('profile')


def remove_artist(request, artist_id):
  gallery_profile = Gallery.objects.get(user=request.user)
  gallery_profile.artists.remove(artist_id)
  gallery_profile.save()
  return redirect('profile')

def remove_gallery(request, gallery_id):
  artist_profile = Artist.objects.get(user=request.user)
  artist_profile.galleries.remove(gallery_id)
  artist_profile.save()
  return redirect('profile')  

# ADD A GALLERY TO AN ARTIST
# def assoc_gallery(request, artist_id, gallery_id):
#   found_artist = Artist.objects.get(id=artist_id)
#   found_artist.galleries.add(gallery_id)
#   return redirect('artist_profile', artist_id = artist_id)

# def assoc_gallery(request, artist_id, gallery_id):
#   found_artist = Artist.objects.get(id=artist_id)
#   found_artist.gallery.add(gallery_id)
#   return redirect('artist_profile', artist_id = artist_id)

  
# def assoc_gallery(request, gallery_id):
#   Artist.objects.get(id=artist_id).galleries.add(gallery_id)
#   return redirect('artist_profile', artist_id=artist_id)