#/usr/bin/env python
# *_* encoding=utf-8 *_*
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from sousaie.blog.views import *

#关于页面
def about_us(request):
    return render_to_response('about_us.html',local())

#登陆
def login_view(request):
	user=authenticate(username=request.POST['username'],password=request.POST['password'])
	if user is not None:
		login(request,user)
		print request.user
		return list_blogs
	else:
		return list_blogs

#登出
def logout_view():
	logout(request)
	return list_blogs
