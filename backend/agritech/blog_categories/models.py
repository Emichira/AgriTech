from django.db import models
from datetime import datetime

class BlogCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    blog_category_image = models.ImageField(upload_to='images/blog/%Y/%m/%d/')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"