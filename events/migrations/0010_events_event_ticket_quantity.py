# Generated by Django 3.1.5 on 2021-02-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_remove_events_event_ticket_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_ticket_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
