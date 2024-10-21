from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import usuarios
from .models import usuarios_videos
from .models import videos

admin.site.register(usuarios)
admin.site.register(usuarios_videos)
admin.site.register(videos)