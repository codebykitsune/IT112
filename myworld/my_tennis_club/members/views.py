from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render, redirect
from .models import BlogPost

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def show_blog(request):
  template  = loader.get_template('blog.html')
  return HttpResponse(template.render())


def works(request):
    return render(request, 'works.html')

def blog(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        
       
        BlogPost.objects.create(title=title, body=body)
        
       
        return redirect('blog') 

    
    posts = BlogPost.objects.all().order_by('-created_at')
    
    context = {
        'posts': posts,
    }
    return render(request, 'blog.html', context)