from django.contrib import admin
from .models import Artist, Gallery, Artist_photo


# Register your models here.
# admin.site.register([Artist, Gallery])
admin.site.register(Artist)
admin.site.register(Gallery)
admin.site.register(Artist_photo)