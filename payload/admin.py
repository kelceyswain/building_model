from django.contrib import admin

# Register your models here.
from .models import Building, Text, Image, Video, Sound

admin.site.register(Building)
admin.site.register(Text)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Sound)
