# Generated by Django 4.0.1 on 2022-08-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_agents', '0002_agent_property_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='best',
            field=models.BooleanField(default=False, verbose_name='Лучший агент'),
        ),
    ]
