from django.contrib import admin
from . models import (
    Events,
    )


class EventsAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'event_name',
                    'event_display_status',
                    'create_at'
                    ]


admin.site.register(Events, EventsAdmin)
