from django.contrib import admin
from .models import Videos
from embed_video.admin import AdminVideoMixin


class VideosAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = [
                    'video',
                    ]


admin.site.register(Videos, VideosAdmin)
