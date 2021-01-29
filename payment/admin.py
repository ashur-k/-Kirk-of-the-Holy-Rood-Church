from django.contrib import admin
from .models import Payment, PaymentLineItem


# Register your models here.
class PaymentLineItemAdminInline(admin.TabularInline):
    model = PaymentLineItem
    readonly_fields = ('lineitem_total',)


class PaymentAdmin(admin.ModelAdmin):
    inlines = (PaymentLineItemAdminInline,)

    readonly_fields = ('payment_number', 'date',
                       'payment_amount', 'payment_total_amount')

    fields = ('payment_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'payment_amount',
              'payment_total_amount')

    list_display = ('payment_number', 'date', 'full_name',
                    'payment_amount', 'payment_total_amount',)

    ordering = ('-date',)


admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentLineItem)
