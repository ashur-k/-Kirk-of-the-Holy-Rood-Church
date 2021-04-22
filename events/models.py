from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Events(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    event_name = models.CharField(max_length=254, null=False, blank=False)
    image = models.ImageField(blank=False, upload_to='media/')
    event_description = models.TextField()
    event_price = models.DecimalField(max_digits=6, decimal_places=2)
    is_free_event = models.BooleanField(default=False)
    event_display_status = models.CharField(max_length=10, choices=STATUS)
    event_instructions = models.CharField(max_length=254, null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name

    def event_dates(self):
        event_dates = EventDates.objects.filter(event_id=self.id)
        return event_dates


class EventDates(models.Model):
    event = models.ForeignKey(
        Events,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    date = models.DateTimeField()
    total_tickets = models.IntegerField(default=1)
    ticket_sold = models.IntegerField(default=0)
    available_tickets = models.IntegerField(default=0)

    def __str__(self):
        return self.event.event_name

    def update_tickets_sold(self, value):
        self.ticket_sold = self.ticket_sold + value
        self.available_tickets = self.total_tickets - self.ticket_sold
        self.save()


class BookingFreeEvents(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    event_title = models.ForeignKey(
        Events,
        null=True, blank=True,
        on_delete=models.SET_NULL)
    event_booking_date = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = PhoneNumberField()
    number_of_bookings = models.IntegerField(
        default=1,
        null=False,
        blank=False)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
