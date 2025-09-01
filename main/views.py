from django.shortcuts import render

def home(request):
	return render(request, 'main/home.html')

def about(request):
	return render(request, 'main/about.html')

def careers(request):
	return render(request, 'main/careers.html')

def contact(request):
	return render(request, 'main/contact.html')

# Create your views here.
