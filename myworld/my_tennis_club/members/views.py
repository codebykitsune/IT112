from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render, redirect
from .models import Post

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def show_base(request):
  template  = loader.get_template('base.html')
  return HttpResponse(template.render())

def timeline(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        if title and body:
            Post.objects.create(title=title, body=body)
        return redirect("timeline")  

   
    posts = Post.objects.order_by("-created_at")
    return render(request, "timeline.html", {"posts": posts})