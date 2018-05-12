# Generated by Django 2.0.4 on 2018-05-12 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newslink',
            options={'get_latest_by': ['pub_date'], 'ordering': ['-pub_date'], 'verbose_name': 'News Article'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(help_text='Enter the <slug></slug>', unique=True, verbose_name='Slug'),
        ),
    ]
