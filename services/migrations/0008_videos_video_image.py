# Generated by Django 3.1.5 on 2021-03-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_sundayserviceinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='video_image',
            field=models.ImageField(default='media/ben-white-vtCBruWoNqo-unsplash_6FJQsPn.jpg', upload_to='media/video_images/'),
            preserve_default=False,
        ),
    ]
