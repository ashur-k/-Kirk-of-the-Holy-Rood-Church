from django.contrib import admin
from .models import Contactus


class ContactusAdmin(admin.ModelAdmin):
    list_display = [
                    'ministy',
                    'full_name',
                    'email',
                    'message',
                    'receieve_at',
                    ]


admin.site.register(Contactus, ContactusAdmin)
