# Generated by Django 3.0.8 on 2020-07-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
