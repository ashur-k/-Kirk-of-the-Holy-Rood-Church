# Generated by Django 3.1.5 on 2021-01-18 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministries', '0020_meetingtimes_meeting_ministry_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingtimes',
            name='week_day',
            field=models.CharField(default='None', max_length=30),
        ),
    ]
