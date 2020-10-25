
from django.shortcuts import render
from django.http import HttpResponse

from .models import Class_User, Image_User, Image_class_picture, Image_Classroom
# class baseview
from django.views import View

# Create your views here.
def list_class(request):
	context = {'list_all': Class_User.objects.all()}
	# return HttpResponse("Heelp")
	return render(request, 'appimage/list_class.html', context)
# display image own member
def image_class(request, list_id):
	context = {'list_member': Class_User.objects.get(id=list_id),
				'list_all': Class_User.objects.all()}
	return render(request, 'appimage/image_member.html', context)

# display image puture in my class
def image_puture_class(request):
	context = {'puture': Image_class_picture.objects.all(),
				'list_all': Class_User.objects.all()}
	return render(request, 'appimage/image_puture.html', context)

# display image inclassroom
def image_classroom(request):
	context = {'classroom': Image_Classroom.objects.all(),
				'list_all': Class_User.objects.all()}
	return render(request, 'appimage/list_in_class.html', context)
