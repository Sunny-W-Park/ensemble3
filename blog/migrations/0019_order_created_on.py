# Generated by Django 3.0.8 on 2020-07-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200728_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
