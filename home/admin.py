from django.contrib import admin
from .models import SiteColorTheme, CurrentColorTheme


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


admin.site.register(SiteColorTheme, SiteColorThemeAdmin)
admin.site.register(CurrentColorTheme, CurrentColorThemeAdmin)
