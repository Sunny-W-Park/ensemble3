# Generated by Django 3.0.8 on 2020-08-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200804_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, max_length=550, null=True, upload_to='blog/images'),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, max_length=550, null=True, upload_to='blog/images'),
        ),
    ]