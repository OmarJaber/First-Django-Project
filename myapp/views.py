from django.shortcuts import render
from .models import student
# Create your views here.

def homepage(request):
	return render(request, 'home.html' , {"name":" Omar Jaber"})

def homepageshow(request):
	data = student.objects.all()
	return render(request, 'home2.html' , {"data": data})

def homepageadd(request):
	data = student.objects.filter(id=1)
	return render(request, 'home.html' , {"data": data})
	
def homeshowfilter(request,count):
	data = student.objects.filter(id=count)
	return render(request, 'home2.html' , {"data": data})
