# Generated by Django 5.0.4 on 2024-04-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_issue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logissue',
            name='category',
            field=models.CharField(choices=[('INF', 'Infrastructure'), ('ENV', 'Environmental'), ('SAF', 'Safety'), ('SOC', 'Social'), ('ECO', 'Economic'), ('EDU', 'Educational'), ('HEA', 'Health'), ('OTH', 'Other')], default='OTH', max_length=3),
        ),
    ]