from django.contrib import admin
from .models import student , level
# Register your models here.

class myapplist(admin.ModelAdmin):
    list_display = ['id','name','mobile','address','selectop','levellink']

admin.site.register(student, myapplist)
admin.site.register(level)