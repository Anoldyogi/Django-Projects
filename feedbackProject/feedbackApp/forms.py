from django import forms
from django.core import validators

def start_with(value):
	if value[0].lower()!='d':
		raise forms.ValidationError("Name shoudl start with d")

class feedbackForm(forms.Form):
	name=forms.CharField(validators=[start_with])
	email=forms.EmailField()
	feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])

	'''def clean_name(self):
		inputname=self.cleaned_data['name']
		if len(inputname)<4:
			raise forms.ValidationError("length is less then 4")
		return inputname

	def clean_email(self):
		inputemail=self.cleaned_data['email']
		print('validating email')
		return inputemail	'''
