from django.shortcuts import render
from . import forms
# Create your views here.
def registerview(request):
	form=forms.studentregister()
	return render(request,'testapp/register.html',{'form':form})
