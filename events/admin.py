from django.contrib import admin
from . models import (
    Events,
    EventDates,
    BookingFreeEvents
    )


class EventDatesAdminInline(admin.TabularInline):
    model = EventDates
    readonly_fields = ('event',)


class EventsAdmin(admin.ModelAdmin):
    inlines = (EventDatesAdminInline,)
    list_display = [
                    'id',
                    'event_name',
                    'event_display_status',
                    'create_at'
                    ]


admin.site.register(Events, EventsAdmin)
admin.site.register(EventDates)
admin.site.register(BookingFreeEvents)
