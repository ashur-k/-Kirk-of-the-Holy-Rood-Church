# Generated by Django 3.1.5 on 2021-02-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20210203_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
    ]
