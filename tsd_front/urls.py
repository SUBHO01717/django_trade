from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='course'),
    path('course_details/<int:id>', views.coursePage, name='course_details'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/<int:id>', views.blogdetails, name='blog_detail'),
    path('our_teachers/', views.teacher, name='our_teachers'),
    path('contact/', views.contactPage, name='contact'),

]