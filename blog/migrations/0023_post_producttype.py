# Generated by Django 3.0.8 on 2020-07-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20200728_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='producttype',
            field=models.ManyToManyField(related_name='posts', to='blog.Product'),
        ),
    ]
