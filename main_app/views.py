from django.shortcuts import render
# from .models import Artist, Gallery


def home(request):
  return render(request, 'home.html')

def artist_index(request):
  return render(request, 'artists/artist_index.html')

def artist_show(request, artist_id):
  return render(request, 'artists/artist_show.html')


def gallery_index(request):
  return render(request, 'galleries/gallery_index.html')

def gallery_show(request, gallery_id):
  return render(request, 'galleries/gallery_show.html')  