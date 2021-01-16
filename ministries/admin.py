from django.contrib import admin
from . models import AlphaGroup, Ministries, MeetingTimes


class MinistriesAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'ministry_heading',
                    ]

class MeetingTimesAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'meeting_times_id',
                    ]

admin.site.register(AlphaGroup)
admin.site.register(Ministries, MinistriesAdmin)
admin.site.register(MeetingTimes, MeetingTimesAdmin)
