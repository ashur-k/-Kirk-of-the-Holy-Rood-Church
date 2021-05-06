from django.db import models


class Contactus(models.Model):
    ministy = models.CharField(max_length=50, default="Contact-Us-Messages")
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    message = models.TextField()
    send_email_to = models.EmailField(default="ashurkanwal@yahoo.com")
    receieve_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
