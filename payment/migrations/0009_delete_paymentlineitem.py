# Generated by Django 3.1.5 on 2021-02-03 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_auto_20210203_0958'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentLineItem',
        ),
    ]
