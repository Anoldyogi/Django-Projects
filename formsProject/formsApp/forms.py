from django import forms

class studentRegister(forms.Form):
	name=forms.CharField()
	marks=forms.IntegerField()
