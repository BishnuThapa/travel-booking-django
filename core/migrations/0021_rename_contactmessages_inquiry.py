# Generated by Django 4.1.7 on 2023-03-27 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_contactmessages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactMessages',
            new_name='Inquiry',
        ),
    ]
