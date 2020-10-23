from django.db import models
from datetime import datetime
from blog_categories.models import BlogCategory

class Blog(models.Model):
    categories = models.ManyToManyField(BlogCategory, blank=True, null=True)
    slug = models.SlugField(unique=True)
    blog_image = models.ImageField(upload_to='images/blog/%Y/%m/%d/')
    title = models.CharField(max_length=200)
    blog_author = models.CharField(max_length=200, blank=True, null=True)
    first_paragraph = models.TextField()
    middle_paragragh = models.TextField(null=True, blank=True)
    final_paragragh = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    reading_time = models.CharField(max_length=2, blank=True, null=True)
    blog_date = models.DateField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def blog_count(self):
        return Blog.objects.filter(blog=self).count()