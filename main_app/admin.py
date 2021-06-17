from django.contrib import admin
from .models import Artist, Gallery


# Register your models here.
# admin.site.register([Artist, Gallery])
admin.site.register(Artist)
admin.site.register(Gallery)