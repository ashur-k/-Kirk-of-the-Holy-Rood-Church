# Generated by Django 3.1.5 on 2021-04-17 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210417_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondparallaxsection',
            name='sunday_services',
        ),
    ]