from django.contrib import admin
from . models import(
    Message,
    Ministries,
    MeetingTimes,
    WeekDays
    )


class MeetingTimesAdminInline(admin.TabularInline):
    model = MeetingTimes
    readonly_fields = ('id',)
    # readonly_fields = ('lineitem_total',)


class MinistriesAdmin(admin.ModelAdmin):
    inlines = (MeetingTimesAdminInline,)

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
