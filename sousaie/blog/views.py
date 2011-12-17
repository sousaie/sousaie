from django.http import HttpResponse
from django.shortcuts import render_to_response
from sousaie.blog.models import *

def list_blogs(request):
    blog = Blog();
    blogs = blog.list_blogs()
    return render_to_response('list_blogs.html',{'blogs':blogs})
