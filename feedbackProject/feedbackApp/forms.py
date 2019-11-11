from django import forms
class feedbackForm(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()
	feedback=forms.CharField(widget=forms.Textarea)

	def clean_name(self):
		inputname=self.cleaned_data['name']
		if len(inputname)<4:
			raise forms.ValidationError("length is less then 4")
		return inputname

	def clean_email(self):
		inputemail=self.cleaned_data['email']
		print('validating email')
		return inputemail	
