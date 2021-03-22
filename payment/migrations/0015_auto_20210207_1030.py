# Generated by Django 3.1.5 on 2021-02-07 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0014_payment_payment_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketspayment',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='payment.payment'),
        ),
    ]