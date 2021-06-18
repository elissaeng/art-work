from django.shortcuts import render, redirect
from .models import Artist, Gallery
from .forms import ArtistForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
      return redirect('artist_show', artist.id)

     

# GALLERY INDEX
def gallery_index(request):
  galleries = Gallery.objects.all()
  return render(request, 'galleries/gallery_index.html')


# GALLERY SHOW
def gallery_show(request, gallery_id):
  return render(request, 'galleries/gallery_show.html')        



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
      return redirect('artists_index')
    else:
      error_message = 'Invalid sign up - please try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)       
