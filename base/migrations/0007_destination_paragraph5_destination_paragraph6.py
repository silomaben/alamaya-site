# Generated by Django 4.2.1 on 2023-06-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_paragraph_destination_paragraph1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='paragraph5',
            field=models.TextField(default='Maasai Mara'),
        ),
        migrations.AddField(
            model_name='destination',
            name='paragraph6',
            field=models.TextField(default='Maasai Mara'),
        ),
    ]
