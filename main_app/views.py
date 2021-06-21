from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import Artist, Gallery
from .forms import ArtistForm, GalleryForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# HOME
def home(request):
  return render(request, 'home.html')


# ARTIST INDEX
def artists_index(request):
  artists = Artist.objects.all()
  context = { 'artists': artists }
  return render(request, 'artists/artists_index.html', context)


# ARTIST SHOW
def artist_show(request, artist_id):
  found_artist = Artist.objects.get(id=artist_id)
  artist_form = ArtistForm()
  context= { 'artist': found_artist, 'ArtistForm': artist_form }

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


# ///////// GALLERIES  ///////////  

# GALLERY INDEX
def gallery_index(request):
  galleries = Gallery.objects.all()
  context = { 'galleries': galleries }
  return render(request, 'galleries/gallery_index.html', context)


# GALLERY SHOW
def gallery_show(request, gallery_id):
  found_gallery = Gallery.objects.get(id=gallery_id)
  gallery_form = GalleryForm()
  context= { 'gallery': found_gallery, 'GalleryForm': gallery_form }

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
  if (artist_profile.count()>0):
    return render(request, 'profile.html', {'profile': artist_profile[0], 'is_gallery': False})
  else: 
    return render(request, 'profile.html', {'profile': gallery_profile[0], 'is_gallery': True})


def artist_show(request, artist_id):
  found_artist = Artist.objects.get(id=artist_id)
  artist_form = ArtistForm()
  context= { 'artist': found_artist, 'ArtistForm': artist_form }

  return render(request, 'artists/artist_show.html', context)
