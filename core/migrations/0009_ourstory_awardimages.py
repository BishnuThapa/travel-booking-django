# Generated by Django 4.1.7 on 2023-03-22 10:01

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_whyus_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Story & Award',
                'verbose_name_plural': 'Story & Awards',
            },
        ),
        migrations.CreateModel(
            name='AwardImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='awards')),
                ('ourstory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ourstory')),
            ],
            options={
                'verbose_name': 'Award',
                'verbose_name_plural': 'Award',
            },
        ),
    ]
