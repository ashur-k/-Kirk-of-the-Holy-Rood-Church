# Generated by Django 3.1.5 on 2021-02-07 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0019_auto_20210207_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketspayment',
            name='payment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='payment.payment'),
            preserve_default=False,
        ),
    ]