# Generated by Django 4.0.1 on 2022-08-14 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eastate_property', '0014_alter_propertygallery_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата публикации'),
        ),
    ]
