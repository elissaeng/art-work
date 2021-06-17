from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('artist', views.artist_index, name='artist_index'),
  path('artist/<int:artist_id>', views.artist_show, name='artist_show'),
]