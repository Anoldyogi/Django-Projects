from django import forms
from django.core import validators

def start_with(value):
	if value[0].lower()!='d':
		raise forms.ValidationError("Name shoudl start with d")

class feedbackForm(forms.Form):
	name=forms.CharField(validators=[start_with])
	email=forms.EmailField()
	password=forms.CharField(widget=forms.PasswordInput)
	rpassword=forms.CharField(label='Password(again)',widget=forms.PasswordInput)
	feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
	bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)
# EXPLICIT CLEAN METHOD VALIDATIONS
''' def clean_name(self):
		inputname=self.cleaned_data['name']
		if len(inputname)<4:
			raise forms.ValidationError("length is less then 4")
		return inputname

	def clean_email(self):
		inputemail=self.cleaned_data['email']
		print('validating email')
		return inputemail	'''
# EXPLICIT SINGLE CLEAN METHOD VALIDATION
'''
	def clean(self):
		cleaned_data=super().clean()
		inputpwd=cleaned_data['password']
		inputrpwd=cleaned_data['rpassword']

		if inputpwd!=inputrpwd:
			raise forms.ValidationError("Password do not match")
'''
###BOT VALIDATION
    def clean(self):
    	print("BOTS BOTS")
    	cleaned_data=super().clean()
    	bot_value=cleaned_data['bot_handler']
    	if len(bot_handler)>0:
	    	raise forms.ValidationError("Thanks Bot")
