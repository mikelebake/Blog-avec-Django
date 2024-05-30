# Generated by Django 5.0 on 2024-05-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='images/blog-1.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='nbre_vues',
            field=models.IntegerField(default=0),
        ),
    ]