# Generated by Django 3.1.5 on 2021-02-06 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20210203_0953'),
        ('payment', '0012_auto_20210206_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='event',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='event_ticket_qty',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_total',
        ),
        migrations.CreateModel(
            name='TicketsPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_ticket_qty', models.IntegerField(default=1)),
                ('payment_total', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.events')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
            ],
        ),
    ]