from django import forms

class studentregister(forms.Form):
	name=forms.CharField()
	marks=forms.IntegerField()
