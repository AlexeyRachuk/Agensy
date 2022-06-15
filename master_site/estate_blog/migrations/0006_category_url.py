# Generated by Django 4.0.1 on 2022-01-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_blog', '0005_remove_category_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.SlugField(default=1, max_length=130, unique=True),
            preserve_default=False,
        ),
    ]