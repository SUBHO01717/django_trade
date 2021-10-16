from django.contrib import admin
from . models import Course,Tag, Prerequisit, Learning, Resource,Teacher, TsdBlog
# Register your models here.

admin.site.register(Course)
admin.site.register(Tag)
admin.site.register(Prerequisit)
admin.site.register(Learning)
admin.site.register(Resource)
admin.site.register(Teacher)
admin.site.register(TsdBlog)