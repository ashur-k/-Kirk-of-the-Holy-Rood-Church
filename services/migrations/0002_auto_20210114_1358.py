# Generated by Django 3.1.5 on 2021-01-14 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='about',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='date',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='status',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='title',
        ),
    ]