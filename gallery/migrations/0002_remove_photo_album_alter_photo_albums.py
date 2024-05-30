# Generated by Django 5.0.6 on 2024-05-30 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='album',
        ),
        migrations.AlterField(
            model_name='photo',
            name='albums',
            field=models.ManyToManyField(related_name='photos', to='gallery.album'),
        ),
    ]