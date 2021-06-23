from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('artists/', views.artists_index, name='artists_index'),
  path('artist/<int:artist_id>/', views.artist_show, name='artist_show'),
  path('artist/new/', views.artist_create, name='artist_create'),
  path('artist/edit/<int:artist_id>/', views.artist_edit, name='artist_edit'),
  path('artist/delete/<int:artist_id>/', views.artist_delete, name='artist_delete'),
  path('artist/add_photo/<int:artist_id>', views.artist_photo, name="artist_photo"),

  path('accounts/signup', views.signup, name='signup'),

  path('gallery/', views.gallery_index, name='gallery_index'),
  path('gallery/<int:gallery_id>/', views.gallery_show, name='gallery_show'),
  path('gallery/edit/<int:gallery_id>/', views.gallery_edit, name='gallery_edit'),
  path('gallery/delete/<int:gallery_id>/', views.gallery_delete, name='gallery_delete'),
   path('gallery/add_photo/<int:gallery_id>', views.gallery_photo, name="gallery_photo"),

  path('profile/', views.profile, name='profile'),

  # path('artists/<int:artist_id>/assoc_gallery/<int:gallery_id>/', views.assoc_gallery, name='assoc_gallery')
  
  path('galleries/<int:gallery_id>/assoc_gallery/', views.assoc_gallery, name='assoc_gallery')

  # path('artist/galleries/', views.assoc_gallery, name='assoc_gallery'),

  # path('galleries/<int:gallery_id>/artist/<int:artist_id>', views.assoc_gallery, name='assoc_gallery')


  # path('gallery/<int:gallery_id>/<int:artist_id>', views.assoc_gallery, name='assoc_gallery')
  # path('gallery/<int:artist_id>/galleries/<int:gallery_id>/', views.assoc_gallery, name='assoc_gallery'),
]

