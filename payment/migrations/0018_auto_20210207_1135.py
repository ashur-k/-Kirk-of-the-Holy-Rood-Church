# Generated by Django 3.1.5 on 2021-02-07 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0017_payment_grand_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_total',
            new_name='ticket_payment_total',
        ),
    ]