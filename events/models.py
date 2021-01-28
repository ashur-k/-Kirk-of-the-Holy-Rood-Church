from django.db import models


class Events(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    event_name = models.CharField(max_length=254, null=False, blank=False)
    image = models.ImageField(blank=False, upload_to='media/')
    event_description = models.TextField()
    event_dates = models.CharField(max_length=254, null=False, blank=False)
    event_buy_button_text = models.CharField(max_length=254, null=False, blank=False)
    event_display_status = models.CharField(max_length=10, choices=STATUS)
    event_instructions = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.event_name
