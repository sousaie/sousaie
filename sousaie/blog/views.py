from django.http import HttpResponse
from django.shortcuts import render_to_response
from sousaie.blog.models import *

def list_blogs(request):
    blog = Blog()
    blogs = blog.list_blogs()
    return render_to_response('list_blogs.html',{'blogs':blogs})

def view_blog_detail(request,entryid):
    if entryid:
        blog = Blog();
        entry = blog.list_blog_detail(entryid)
        print "view_entry_content:%s,title:%s," % (entry.content,entry.title)
        return render_to_response('list_blog_detail.html',{'blog':entry})
    else:
         return None
