from django import forms
from .models import Artist

class ArtistForm(forms.ModelForm):
  class Meta:
    model = Artist
    fields = ('name', 'location', 'bio', 'img_urls', 'highlights', 'fun_fact', 'user', 'website')
 