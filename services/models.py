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
