# Generated by Django 4.1.7 on 2023-03-21 06:28

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True,
                 max_length=255, null=True, unique=True)),
                ('featured_image', models.ImageField(upload_to='blog')),
                ('description', ckeditor.fields.RichTextField()),
                ('readtime', models.CharField(blank=True,
                 help_text='eg: 5 min', max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ImageField(blank=True,
                 default='', null=True, upload_to='images')),
                ('logo', models.ImageField(blank=True,
                 default='', null=True, upload_to='images')),
                ('phone', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('secondary_email', models.EmailField(
                    blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100)),
                ('short_description', models.TextField(
                    blank=True, max_length=255, null=True)),
                ('location_map', models.TextField(blank=True, null=True)),
                ('footer_text_copyright', models.CharField(
                    blank=True, default='', max_length=100, null=True)),
                ('footer_copyright_url', models.URLField(
                    blank=True, default='', null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('meta_title', models.CharField(blank=True,
                 default='', max_length=255, null=True)),
                ('meta_keyword', models.TextField(blank=True, null=True)),
                ('meta_description', ckeditor.fields.RichTextField(
                    blank=True, null=True)),
            ],
            options={
                'verbose_name': 'General Setting',
                'verbose_name_plural': 'General Setting',
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True,
                 max_length=100, null=True, unique=True)),
                ('featured_image', models.ImageField(
                    help_text='1920*1280 px', upload_to='destination')),
                ('description', ckeditor.fields.RichTextField()),
                ('ordering', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Destination',
                'verbose_name_plural': 'Destination',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(
                    help_text='1920*1280 px', upload_to='slider')),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_heading', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slider',
            },
        ),
        migrations.CreateModel(
            name='Tour_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True,
                 max_length=255, null=True, unique=True)),
                ('icon', models.ImageField(upload_to='tour_type')),
                ('image', models.ImageField(upload_to='tour_type')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('destination', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.destination')),
            ],
            options={
                'verbose_name': 'Tour Category',
                'verbose_name_plural': 'Tour Category',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True,
                 max_length=255, null=True, unique=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('publish', models.CharField(blank=True, choices=[
                 ('Enable', 'Enable'), ('Disable', 'Disable')], default=1, max_length=15, null=True)),
                ('featured_image', models.ImageField(upload_to='tour')),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('difficulty', models.CharField(blank=True, choices=[
                 ('Low', 'Low'), ('Moderate', 'Moderate'), ('High', 'High')], default='Low', max_length=50, null=True)),
                ('max_altitude', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('trip_start', models.CharField(blank=True,
                 default='Kathmandu', max_length=100, null=True)),
                ('trip_end', models.CharField(blank=True,
                 default='Kathmandu', max_length=100, null=True)),
                ('group_size', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('meals', models.TextField(blank=True, null=True)),
                ('accomodation', models.TextField(blank=True, null=True)),
                ('regular_price', models.IntegerField(blank=True, null=True)),
                ('sell_price', models.IntegerField(blank=True, null=True)),
                ('overview', ckeditor.fields.RichTextField()),
                ('includes', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('excludes', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('activity', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.tour_type')),
                ('destination', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.destination')),
            ],
            options={
                'verbose_name': 'Tour',
                'verbose_name_plural': 'Tour',
            },
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('tour', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.tour')),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=255, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('tour', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.tour')),
            ],
        ),
        migrations.CreateModel(
            name='Cultural_Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('tour', models.ManyToManyField(to='core.tour')),
            ],
            options={
                'verbose_name': 'Cultural Tour',
                'verbose_name_plural': 'Cultural Tour',
            },
        ),
    ]
