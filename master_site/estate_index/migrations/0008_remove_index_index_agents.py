# Generated by Django 4.0.1 on 2022-08-14 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate_index', '0007_index_facebook_index_instagram_index_twitter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='index_agents',
        ),
    ]