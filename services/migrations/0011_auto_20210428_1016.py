# Generated by Django 3.1.5 on 2021-04-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_videos_pinned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='title',
            field=models.CharField(default='New Video', max_length=50),
        ),
    ]