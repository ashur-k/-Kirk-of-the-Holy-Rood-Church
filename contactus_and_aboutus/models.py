from django.db import models


class Contactus(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    message = models.TextField()
    receieve_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
