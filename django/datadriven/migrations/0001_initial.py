# Generated by Django 3.2.6 on 2021-08-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('link', models.URLField(blank=True, null=True)),
                ('order', models.IntegerField(default=100)),
                ('admin_published', models.BooleanField(default=False)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'ordering': ['order', 'name', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('fontawesome_icon', models.CharField(blank=True, max_length=100, null=True)),
                ('order', models.IntegerField(default=100)),
                ('admin_published', models.BooleanField(default=False)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'ordering': ['order', 'name', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('message_text', models.TextField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('author', models.ManyToManyField(blank=True, db_table='datadriven_m2m_message_service', related_name='message', to='datadriven.Service')),
            ],
            options={
                'ordering': ['-meta_created_datetime', '-id'],
            },
        ),
    ]