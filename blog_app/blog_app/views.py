from django.shortcuts import render, redirect
from blog import views

def redirect_blog(request):
    return redirect('blog_home', permanent=True)