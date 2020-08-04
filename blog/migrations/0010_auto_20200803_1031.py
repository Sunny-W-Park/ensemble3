# Generated by Django 3.0.8 on 2020-08-03 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200802_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='order_count',
        ),
        migrations.AlterField(
            model_name='post',
            name='call',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='call_rate',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='inventory',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='제목'),
        ),
    ]