from django import forms
from .models import Artist, Gallery


class ArtistForm(forms.ModelForm):
  class Meta:
    model = Artist
    fields = ('name', 'location', 'bio', 'profile_img', 'highlights', 'fun_fact', 'website')
 

class GalleryForm(forms.ModelForm):
  class Meta:
    model = Gallery
    fields = ('name', 'location', 'bio', 'profile_img', 'highlights', 'fun_fact', 'website') 