# Generated by Django 3.0.8 on 2020-08-05 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200804_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='inventory',
        ),
        migrations.AlterField(
            model_name='post',
            name='call',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='주문량'),
        ),
        migrations.AlterField(
            model_name='post',
            name='call_rate',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='쿠폰펀딩률'),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=0, null=True, verbose_name='가격'),
        ),
    ]