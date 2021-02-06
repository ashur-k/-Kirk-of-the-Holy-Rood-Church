# Generated by Django 3.1.5 on 2021-02-02 11:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20210129_1842'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentlineitem',
            name='payment',
        ),
        migrations.AddField(
            model_name='paymentlineitem',
            name='event_payment_order_number',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paymentlineitem',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.events'),
        ),
    ]
