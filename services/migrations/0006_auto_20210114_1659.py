# Generated by Django 3.1.5 on 2021-01-14 16:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20210114_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videos',
            name='main_paragraph',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='videos',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=10),
        ),
        migrations.AddField(
            model_name='videos',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
