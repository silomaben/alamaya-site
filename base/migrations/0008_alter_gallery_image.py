# Generated by Django 4.2.4 on 2023-08-25 17:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_destination_paragraph5_destination_paragraph6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
