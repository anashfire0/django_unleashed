from django.db import models
from organizer.models import Tag, StartUp
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

    title = models.CharField('Title', max_length=264)
    slug = models.SlugField('Slug', unique_for_month='pub_date')
    text = models.TextField('Text')
    pub_date = models.DateField('Published Date', auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='blog_posts')
    startups = models.ManyToManyField(
        StartUp, related_name='blog_posts',blank=True,)

    def __str__(self):
        return f'{self.title} on {self.pub_date:%Y-%m-%d}'

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    def get_update_url(self):
        return reverse('blog_post_update', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    def get_delete_url(self):
        return reverse('blog_post_delete', args=[self.pub_date.year, self.pub_date.month, self.slug])
