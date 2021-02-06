from django.contrib import admin
from .models import Payment, TicketsPayment


class PaymentAdmin(admin.ModelAdmin):

    readonly_fields = ('payment_number', 'date',)

    fields = ('payment_number', 'date', 'full_name',
              'email', 'phone_number',
              'donation_payment_amount',
              )

    list_display = ('payment_number', 'date', 'full_name',
                    'donation_payment_amount',)

    ordering = ('-date',)


admin.site.register(Payment, PaymentAdmin)
admin.site.register(TicketsPayment)
