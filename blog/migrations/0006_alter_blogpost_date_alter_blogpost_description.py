# Generated by Django 5.0 on 2024-05-11 20:22

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_image_blogpost_nbre_vues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
