# Generated by Django 3.0.10 on 2020-11-29 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_remove_post_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_file',
            field=models.ImageField(blank=True, default='board/book.jpg', upload_to='board/post/%Y/%m/d'),
        ),
    ]
