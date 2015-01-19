from django import forms
import datetime

class ApptForm(forms.Form):
	name = forms.CharField(max_length=100)
	phone = forms.CharField(max_length=100)
	address = forms.CharField(max_length=100, required=False)
	zip = forms.IntegerField(required=False)
	email = forms.EmailField(required=False)
	preferred = forms.CharField(max_length=100, required=False)
	message = forms.CharField(required=False)
	ipAddress = forms.IPAddressField()
	dateTime = forms.DateTimeField(initial=datetime.datetime.now())