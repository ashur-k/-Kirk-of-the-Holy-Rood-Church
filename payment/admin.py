from django.contrib import admin
from .models import Payment, TicketsPayment


class TicketsPaymentAdminInline(admin.TabularInline):
    model = TicketsPayment
    readonly_fields = ('lineitem_total',)


class PaymentAdmin(admin.ModelAdmin):

    inlines = (TicketsPaymentAdminInline,)

    readonly_fields = ('payment_number', 'date',
                       'ticket_payment_total', 'grand_total',)

    fields = ('payment_number', 'date', 'full_name',
              'email', 'phone_number',
              'donation_payment_amount', 'ticket_payment_total',
              'grand_total',
              )

    list_display = ('payment_number', 'date', 'full_name',
                    'donation_payment_amount',)

    ordering = ('-date',)


admin.site.register(Payment, PaymentAdmin)
admin.site.register(TicketsPayment)
