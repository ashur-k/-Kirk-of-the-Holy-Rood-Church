from django.contrib import admin
from . models import(
    Message,
    Ministries,
    MeetingTimes,
    WeekDays
    )


class MinistriesAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'ministry_heading',
                    ]


class MeetingTimesAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'meeting_day',
                    ]


class WeekDaysAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'day_name',
                    ]


admin.site.register(Message)
admin.site.register(Ministries, MinistriesAdmin)
admin.site.register(MeetingTimes, MeetingTimesAdmin)
admin.site.register(WeekDays, WeekDaysAdmin)
