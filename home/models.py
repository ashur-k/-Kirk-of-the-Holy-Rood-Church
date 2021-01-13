from django.db import models
from django.utils.safestring import mark_safe


class SiteColorTheme(models.Model):

    theme_name = models.CharField(max_length=20)

    primary_background_color_code = models.CharField(
        max_length=10, blank=True, null='True')

    primary_foreground_color_code = models.CharField(
        max_length=10, blank=True, null='True')

    secondary_background_color_code = models.CharField(
        max_length=10, blank=True, null='True')

    secondary_foreground_color_code = models.CharField(
        max_length=10, blank=True, null='True')

    class Meta:
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.theme_name

    def primary_color_tag(self):
        if self.primary_background_color_code is not None:
            return mark_safe(
                '<p style="background-color:{}">Color </p>'.format(
                    self.primary_background_color_code))
        else:
            return ""

    def secondary_color_tag(self):
        if self.secondary_background_color_code is not None:
            return mark_safe(
                '<p style="background-color:{}">Color </p>'.format(
                    self.secondary_background_color_code))
        else:
            return ""


class CurrentColorTheme(models.Model):
    current_color_theme = models.ForeignKey(
                                            SiteColorTheme,
                                            on_delete=models.CASCADE)


class HeroSectionText(models.Model):
    hero_heading = models.TextField(max_length=200, null=False, blank=False)


class CarouselInnerSection(models.Model):
    carousel_image = models.ImageField(blank=False, upload_to='media/')
    heading = models.CharField(max_length=20, null=False, blank=False)
    paragraph = models.TextField(max_length=250, null=False, blank=False)


class CarouselSectionText(models.Model):
    heading = models.CharField(max_length=20, null=False, blank=False)
    paragraph = models.TextField(max_length=140, null=False, blank=False)


class SecondParallaxSection(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    main_paragraph = models.TextField(max_length=250, null=False, blank=False)
    instruction_paragraph = models.TextField(max_length=65, null=False, blank=False)


class StudyGroupText(models.Model):
    heading = models.CharField(max_length=20, null=False, blank=False)
    paragraph = models.TextField(max_length=200, null=False, blank=False)