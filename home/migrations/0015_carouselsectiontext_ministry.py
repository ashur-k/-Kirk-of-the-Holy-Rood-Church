# Generated by Django 3.1.5 on 2021-04-17 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ministries', '0023_remove_meetingtimes_week_day'),
        ('home', '0014_auto_20210113_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselsectiontext',
            name='ministry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ministries.ministries'),
        ),
    ]
