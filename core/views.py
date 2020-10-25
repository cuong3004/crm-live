from django.shortcuts import render
from django.http import HttpResponse
from appimage.models import Class_User
# app user

# Create your views here.
def Index(request):
	context = {
				'list_all': Class_User.objects.all()}
	return render(request, 'homepage/index.html', context)


