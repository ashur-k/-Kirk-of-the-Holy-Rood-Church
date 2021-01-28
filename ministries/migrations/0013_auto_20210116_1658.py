# Generated by Django 3.1.5 on 2021-01-16 16:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ministries', '0012_auto_20210116_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='ministy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ministries.ministries'),
        ),
        migrations.AlterField(
            model_name='message',
            name='postcode',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='street_address1',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='street_address2',
            field=models.CharField(blank=True, default=43, max_length=80),
            preserve_default=False,
        ),
    ]