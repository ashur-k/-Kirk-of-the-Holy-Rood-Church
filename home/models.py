from django.db import models
from django.utils.safestring import mark_safe


class SiteColorTheme(models.Model):

    theme_name = models.CharField(max_length=20)
    primary_background_color_code = models.CharField(max_length=10, blank=True, null='True')
    primary_foreground_color_code = models.CharField(max_length=10, blank=True, null='True')
    secondary_background_color_code = models.CharField(max_length=10, blank=True, null='True')
    secondary_foreground_color_code = models.CharField(max_length=10, blank=True, null='True')

    class Meta:
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.theme_name

    def primary_color_tag(self):
        if self.primary_background_color_code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.primary_background_color_code))
        else:
            return ""

    def secondary_color_tag(self):
        if self.secondary_background_color_code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.secondary_background_color_code))
        else:
            return ""


class CurrentColorTheme(models.Model):
    current_color_theme = models.ForeignKey(SiteColorTheme, on_delete=models.CASCADE)
