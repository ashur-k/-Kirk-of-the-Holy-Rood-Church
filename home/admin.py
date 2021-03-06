from django.contrib import admin
from .models import (
    SiteColorTheme,
    CurrentColorTheme,
    HeroSectionText,
    CarouselSectionText,
    CarouselInnerSection,
    SecondParallaxSection,
    StudyGroupText,
)


class SiteColorThemeAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'theme_name',
                    'primary_background_color_code',
                    'primary_foreground_color_code',
                    'secondary_background_color_code',
                    'secondary_foreground_color_code',
                    'primary_color_tag',
                    'secondary_color_tag'
                    ]


class CurrentColorThemeAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'current_color_theme',
                    ]


class CarouselSectionTextAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'heading',
                    'paragraph'
                    ]


admin.site.register(SiteColorTheme, SiteColorThemeAdmin)
admin.site.register(CurrentColorTheme, CurrentColorThemeAdmin)
admin.site.register(HeroSectionText)
admin.site.register(CarouselInnerSection)
admin.site.register(CarouselSectionText, CarouselSectionTextAdmin)
admin.site.register(SecondParallaxSection)
admin.site.register(StudyGroupText)
