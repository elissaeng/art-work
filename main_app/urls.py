from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('artist', views.artist_index, name='artist_index'),
  path('artist/<int:artist_id>', views.artist_show, name='artist_show'),
  path('artist/new/', views.artist_create, name='artist_create'),

  path('gallery', views.gallery_index, name='gallery_index'),
  path('gallery/<int:gallery_id>', views.gallery_show, name='gallery_show'),
]