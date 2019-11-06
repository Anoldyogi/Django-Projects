from django.shortcuts import render
from . import forms
# Create your views here.
def feedbackView(request):
	form=forms.feedbackForm()
	if request.method=="POST":
		form=forms.feedbackForm(request.POST)
		if form.is_valid():
			print("Form Validation is success and we are printing the data")
			print("Name is ", form.cleaned_data['name'])
			print("Email is ", form.cleaned_data['email'])
			print("Feedback is ", form.cleaned_data['feedback'])

	return render (request,'testapp/feedback.html',{'form':form})