# Generated by Django 3.1.5 on 2021-04-25 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_and_aboutus', '0005_contactus_send_email_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='name',
            new_name='full_name',
        ),
    ]
