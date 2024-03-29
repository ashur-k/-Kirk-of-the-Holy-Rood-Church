from django.db import models
from embed_video.fields import EmbedVideoField
from phonenumber_field.modelfields import PhoneNumberField


class Videos(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=50, default="New Video", blank=False)
    video = EmbedVideoField()  # same like models.URLField()
    video_image = models.ImageField(
        blank=False,
        upload_to='media/video_images/'
        )
    main_paragraph = models.TextField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    pinned = models.BooleanField(default=False)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def pin(self):
        self.pinned = True
        self.save()

    def unpin(self):
        self.pinned = False 
        self.save()


class SundayServiceInformation(models.Model):
    title = models.CharField(max_length=50, default="Service title")
    preacher_name = models.CharField(max_length=50, default="Preacher Name")
    sermon_title = models.CharField(max_length=100, default="Sermon title")
    bible_refrence = models.TextField(blank=True)
    worship_hymm1 = models.CharField(max_length=100, default="Hymm 1")
    worship_hymm2 = models.CharField(max_length=100, default="Hymm 2")
    worship_hymm3 = models.CharField(max_length=100, default="Hymm 3")
    worship_hymm4 = models.CharField(max_length=100, default="Hymm 4")
    important_notices = models.CharField(max_length=300, default="Notices")
    available_bookings = models.IntegerField(default=50)
    date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def update_available_bookings(self, number_of_bookings):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.available_bookings = self.available_bookings - number_of_bookings
        self.save()

    def update_deleted_bookings(self, number_of_bookings):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.available_bookings = self.available_bookings + number_of_bookings
        self.save()

    def reset_booking_counter(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.available_bookings = 50
        self.save()


class SundayServiceBooking(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)

    service_title = models.ForeignKey(
        SundayServiceInformation,
        null=True, blank=True,
        on_delete=models.SET_NULL)

    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = PhoneNumberField()
    number_of_bookings = models.IntegerField(
        default=1,
        null=False,
        blank=False)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
