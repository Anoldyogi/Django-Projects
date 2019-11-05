from django.shortcuts import render
from . import forms
# Create your views here.
def registerview(request):
	form=forms.studentRegister()
	return render(request,'formsApp/register.html',{'form':form})
