# Generated by Django 3.1.5 on 2021-01-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministries', '0017_auto_20210118_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingtimes',
            name='week_day',
            field=models.CharField(choices=[('To be updated', 'To be updated'), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Satarday', 'Satarday')], default='None', max_length=30),
        ),
    ]
