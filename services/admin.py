from django.contrib import admin
from .models import Videos, SundayServiceInformation
from embed_video.admin import AdminVideoMixin


class VideosAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = [
                    'video',
                    ]


class SundayServiceInformationAdmin(admin.ModelAdmin):
    list_display = [
                    'title',
                    'preacher_name',
                    'sermon_title',
                    'date'
                    ]


admin.site.register(Videos, VideosAdmin)
admin.site.register(
    SundayServiceInformation,
    SundayServiceInformationAdmin
    )
