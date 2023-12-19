from django.contrib import admin

# Register your models here.
from .models import Video, Gallery, Destination,Post


admin.site.register(Video)
admin.site.register(Gallery)
admin.site.register(Destination)
admin.site.register(Post)

