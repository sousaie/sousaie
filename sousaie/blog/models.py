#/usr/bin/env python
# *_* encoding=utf-8 *_*
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=20)
    pub_time= models.CharField(max_length=14)
    description = models.TextField()
    #查询所有blog
    def list_blogs(self):
        try:
            blogs = Blog.objects.all()
        except:
            pass
        return blogs
    #查询每个blog的详细
    def list_blog_detail(self,entry_id):
        print "entry_id:%s" % entry_id
        try:
            entry = Blog.objects.get(id=entry_id)
            print "entry:%s" % entry
        except:
            pass
            entry=None
        return entry
    
    def __unicode__(self):
        return self.title
