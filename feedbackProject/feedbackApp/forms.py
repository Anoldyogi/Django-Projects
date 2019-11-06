from django import forms
class feedbackForm(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()
	feedback=forms.CharField(widget=forms.Textarea)
