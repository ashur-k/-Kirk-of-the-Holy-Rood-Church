# Generated by Django 3.1.5 on 2021-02-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20210202_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_ticket_quantity',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
