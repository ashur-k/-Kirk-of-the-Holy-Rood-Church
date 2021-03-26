from django.db import models
from embed_video.fields import EmbedVideoField


class Videos(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=30, null=False, blank=False)
    video = EmbedVideoField()  # same like models.URLField()
    main_paragraph = models.TextField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class SundayServiceInformation(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    preacher_name = models.CharField(max_length=50, null=False, blank=False)
    sermon_title = models.CharField(max_length=100, null=False, blank=False)
    bible_refrence = models.TextField(blank=True)
    worship_hymm1 = models.CharField(max_length=100)
    worship_hymm2 = models.CharField(max_length=100)
    worship_hymm3 = models.CharField(max_length=100)
    worship_hymm4 = models.CharField(max_length=100)
    important_notices = models.CharField(max_length=300)
    date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
