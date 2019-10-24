from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobs(request):
	h1="<h1> welcome to hyderbad jobs</h1>"
	return HttpResponse(h1)


def chenjobs(request):
	h1="<h1> welcome to chennai jobs</h1>"
	return HttpResponse(h1)

def punejobs(request):
	h2="<h1> welcome to pune jobs</h1>"
	return HttpResponse(h2)
