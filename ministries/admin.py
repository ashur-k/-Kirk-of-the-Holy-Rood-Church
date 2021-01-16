from django.contrib import admin
from . models import Message, Ministries, MeetingTimes


class MinistriesAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'ministry_heading',
                    ]


class MeetingTimesAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'meeting_times_id',
                    'meeting_times',
                    ]


admin.site.register(Message)
admin.site.register(Ministries, MinistriesAdmin)
admin.site.register(MeetingTimes, MeetingTimesAdmin)
