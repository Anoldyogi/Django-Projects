from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,"advanceTemplateApp/home.html")
def sports(request):
	return render(request,"advanceTemplateApp/sports.html")
def movies(request):
	return render(request,"advanceTemplateApp/movies.html")
def politics(request):
	return render(request,"advanceTemplateApp/politics.html")
