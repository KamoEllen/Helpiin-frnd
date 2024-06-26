# Generated by Django 5.0.4 on 2024-04-29 01:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LogIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_title', models.CharField(max_length=255)),
                ('issue_description', models.TextField()),
                ('street_name', models.CharField(blank=True, max_length=255, null=True)),
                ('city_name', models.CharField(max_length=255)),
                ('town_name', models.CharField(blank=True, max_length=255, null=True)),
                ('suburb_name', models.CharField(max_length=255)),
                ('municipality', models.CharField(max_length=255)),
                ('state_name', models.CharField(max_length=100)),
                ('address_type', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=15)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'log_issue',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/')),
                ('log_issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='log_issue.logissue')),
            ],
            options={
                'db_table': 'media_files',
            },
        ),
    ]
