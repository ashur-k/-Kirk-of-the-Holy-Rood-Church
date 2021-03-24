from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Notice(models.Model):

    class Meta:
        verbose_name_plural = 'Notices'
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    notice_title = models.CharField(max_length=100, null=False, blank=False)
    notice_given_by = models.CharField(max_length=50, null=False, blank=False)
    notice_context = models.TextField(max_length=500, null=False, blank=False)
    contact_phone_number = PhoneNumberField()
    contact_email = models.EmailField(max_length=50, null=False, blank=False)
    date_time = models.DateTimeField()
    notice_display_status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notice_title
