#/usr/bin/env python
# *_* encoding=utf-8 *_*
from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField('admin',default='admin',max_length=20)
    description = models.TextField()
    title = models.CharField(max_length=100)
    def get_title_by_user():
        try:
            blogs = Blog.objects.all()
        except:
            pass
        return blogs
    def __unicode__(self):
        return self.title
