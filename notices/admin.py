from django.contrib import admin
from .models import Notice, NewsLetter


class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'notice_title',
        'notice_given_by',
        'notice_context',
        'contact_phone_number',
        'contact_email',
        'date_time',
        'notice_display_status',
        'create_at',
        'update_at',
    )


admin.site.register(Notice, NoticeAdmin)
admin.site.register(NewsLetter)

