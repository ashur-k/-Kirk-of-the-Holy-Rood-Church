# Generated by Django 3.1.5 on 2021-04-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_and_aboutus', '0003_remove_contactus_admin_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='title',
            field=models.CharField(default='Contact-Us-Messages', max_length=50),
        ),
    ]
