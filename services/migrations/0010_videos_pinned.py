# Generated by Django 3.1.5 on 2021-04-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20210329_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]