from django.shortcuts import render
from .models import Artist, Gallery
from .forms import ArtistForm

# HOME
def home(request):
  return render(request, 'home.html')


# ARTIST INDEX
def artist_index(request):
  artists = Artist.objects.all()
  return render(request, 'artists/artist_index.html')


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
  # else:
  #   form = ArtistForm(request.POST)
  #   if form.is_valid():
  #     artist = form.save(commit=False)
  #     artist.user = request.user
  #     artist.save()
  #     return redirect('artist_show', artist.id)



# GALLERY INDEX
def gallery_index(request):
  galleries = Gallery.objects.all()
  return render(request, 'galleries/gallery_index.html')


# GALLERY SHOW
def gallery_show(request, gallery_id):
  return render(request, 'galleries/gallery_show.html')        
