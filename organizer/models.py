from django.db import models
from django.urls import reverse 
# Create your models here.


class Tag(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField('Name', max_length=50, db_index=True)
    slug = models.SlugField('Slug', unique=True,
                            help_text='Enter the slug')

    def get_absolute_url(self):
        return reverse('organizer_tag_detail', args=[self.slug])

    def get_update_url(self):
        return reverse('organizer_tag_update', args=[self.slug])

    def get_delete_url(self):
        return reverse('organizer_tag_delete', args=[self.slug])

    def __str__(self):
        return self.name


class StartUp(models.Model):
    class Meta:
        ordering = ['name']
        get_latest_by = ['founded_date']

    name = models.CharField('Name', max_length=50)
    slug = models.SlugField('Slug', unique=True)
    description = models.TextField('Description')
    founded_date = models.DateField('Founded on')
    contact = models.EmailField('Email')
    website = models.URLField('Website')
    tag = models.ManyToManyField(Tag,)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organizer_startup_detail', args=[self.slug])

    def get_update_url(self):
        return reverse('organizer_startup_update', args=[self.slug])

    def get_delete_url(self):
        return reverse('organizer_startup_delete', args=[self.slug])


class NewsLink(models.Model):
    class Meta:
        verbose_name = 'News Article'
        ordering = ['-pub_date']
        get_latest_by = ['pub_date']

    title = models.CharField('Title', max_length=50)
    pub_date = models.DateField('Published on')
    link = models.URLField('Link')
    startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}:{self.startup}'

    def get_absolute_url(self):
        return self.startup.get_absolute_url()

    def get_update_url(self):
       return reverse('organizer_newslink_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('organizer_newslink_delete', args=[self.pk])