# Generated by Django 3.1.5 on 2021-02-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_auto_20210202_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]