# Generated by Django 3.0.5 on 2021-03-23 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_auto_20210323_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='height_field_r',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_resized',
        ),
        migrations.RemoveField(
            model_name='story',
            name='width_field_r',
        ),
    ]
