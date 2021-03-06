# Generated by Django 3.1.5 on 2021-01-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministries', '0005_auto_20210116_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupheadings',
            name='bible_verse',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='groupheadings',
            name='group_leader',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='groupheadings',
            name='group_leader_info',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='groupheadings',
            name='group_promotion',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='groupheadings',
            name='important_information',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='meetingtimes',
            name='week_day',
            field=models.CharField(choices=[('To be updated', 'To be updated'), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Satarday', 'Satarday')], default='None', max_length=30),
        ),
    ]
