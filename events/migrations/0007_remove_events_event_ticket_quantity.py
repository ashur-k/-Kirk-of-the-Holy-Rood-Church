# Generated by Django 3.1.5 on 2021-02-02 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20210202_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='event_ticket_quantity',
        ),
    ]