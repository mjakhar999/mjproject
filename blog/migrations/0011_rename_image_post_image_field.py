# Generated by Django 3.2.10 on 2021-12-13 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_delete_ormq'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='image_field',
        ),
    ]