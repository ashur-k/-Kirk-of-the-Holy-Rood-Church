# Generated by Django 3.1.5 on 2021-05-11 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0006_auto_20210428_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='title',
            field=models.CharField(default='Notices Title', max_length=50),
        ),
    ]