# Generated by Django 3.1.5 on 2021-02-02 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20210202_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentlineitem',
            name='payment_total',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
