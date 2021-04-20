from django.db import models


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
    event_ticket_quantity = models.IntegerField(default=1)
    event_remaining_ticket = models.IntegerField(default=0)
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
