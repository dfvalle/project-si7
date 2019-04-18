from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')
	
def profile(request):
	return render(request, 'html/profile.html')

def cars(request):
	return render(request, 'html/cars.html')
	
def accessories(request):
	return render(request, 'html/accessories.html')