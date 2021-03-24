# Generated by Django 3.1.5 on 2021-03-24 12:39

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_title', models.CharField(max_length=50)),
                ('notice_give_by', models.CharField(max_length=50)),
                ('notice_context', models.TextField(max_length=500)),
                ('contact_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('contact_email', models.EmailField(max_length=50)),
                ('date', models.DateTimeField()),
                ('notice_display_status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
