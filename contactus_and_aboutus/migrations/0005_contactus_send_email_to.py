# Generated by Django 3.1.5 on 2021-04-25 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_and_aboutus', '0004_contactus_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='send_email_to',
            field=models.EmailField(default='ashurkanwal@yahoo.com', max_length=254),
        ),
    ]
