# Generated by Django 3.1 on 2020-08-06 06:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200806_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hitcount',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 6, 6, 3, 20, 301243, tzinfo=utc), null=True),
        ),
    ]
