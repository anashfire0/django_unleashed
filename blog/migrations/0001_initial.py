# Generated by Django 2.0.4 on 2018-05-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264, verbose_name='Title')),
                ('slug', models.SlugField(unique_for_month='pub_date', verbose_name='Slug')),
                ('text', models.TextField(verbose_name='Text')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Published Date')),
                ('startups', models.ManyToManyField(related_name='blog_posts', to='organizer.StartUp')),
                ('tags', models.ManyToManyField(related_name='blog_posts', to='organizer.Tag')),
            ],
            options={
                'verbose_name': 'blog post',
                'ordering': ['-pub_date', 'title'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]