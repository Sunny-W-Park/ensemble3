# Generated by Django 3.1 on 2020-08-06 12:44

from django.db import migrations, models
import hitcount.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hitcount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
    ]
