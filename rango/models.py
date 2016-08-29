from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        """   Method for saving slugs on save of object"""
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    class Meta:
        """A verbose name for plural category item listings"""
        verbose_name_plural = 'categories'
        def __str__(self):
            return unicode(self.name)

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length = 128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return unicode(self.title)
