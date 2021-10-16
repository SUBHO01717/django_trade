from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator,EmptyPage
from .models import Course, Tag, Prerequisit, Resource,Learning,TsdBlog,Teacher

# Create your views here.

def index(request):
 
  obj= Course.objects.all()
  blog_data= TsdBlog.objects.all()
  
  p= Paginator (blog_data,3)
  page_num = request.GET.get('page',1)

  try:
      page = p.page(page_num)
  except EmptyPage:
      page = p.page(1)

  context ={'obj': obj ,  'blog_data': page } 
  return render(request, 'front_end/index.html',context)

def about(request):
    
  return render(request, 'front_end/about.html',)

def courses(request):
    obj= Course.objects.all()
    context ={'obj': obj}
    return render(request, 'front_end/courses.html',context)

def coursePage(request,id):
  obj= Course.objects.get(pk=id)
  context ={'obj': obj}
 
  return render(request, 'front_end/course_details.html',context)

def blog(request):
    blog_data= TsdBlog.objects.all()
    p= Paginator (blog_data,6)
    page_num = request.GET.get('page',1)
    try:
      page = p.page(page_num)
    except EmptyPage:
      page = p.page(1)
    context ={'blog_data': page}
    return render(request, 'front_end/blog.html',context)

def blogdetails(request,id):
    blog_data= TsdBlog.objects.get(pk=id)
    context ={'blog_data': blog_data}
    return render(request, 'front_end/blog_details.html',context)

def teacher(request):
    t_data= Teacher.objects.all()
    context ={'t_data': t_data}
    return render(request, 'front_end/teacher.html',context)

def contactPage(request):
    
  return render(request, 'front_end/contact.html',)