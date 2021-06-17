from django.shortcuts import render



def home(request):
  return render(request, 'home.html')

def artist_index(request):
  return render(request, 'artists/artist_index.html')

def artist_show(request, artist_id):
  return render(request, 'artists/artist_show.html')
