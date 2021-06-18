from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('artists/', views.artists_index, name='artists_index'),
  path('artist/<int:artist_id>/', views.artist_show, name='artist_show'),
  path('artist/new/', views.artist_create, name='artist_create'),
  path('artist/edit/<int:artist_id>/', views.artist_edit, name='artist_edit'),

  path('accounts/signup', views.signup, name='signup'),

  path('gallery/', views.gallery_index, name='gallery_index'),
  path('gallery/<int:gallery_id>/', views.gallery_show, name='gallery_show'),
]