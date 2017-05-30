from django.contrib import admin
from models import *

# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk','name','gender','age','isDelete']

admin.site.register(student,BookInfoAdmin)
