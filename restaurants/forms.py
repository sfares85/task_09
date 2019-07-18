from django import forms
from .models import Restaurant
from django.contrib.auth.models import User

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }

def __str__(self):
	return self.title


class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username", "password"]
		widgets = {
		"password" : forms.PasswordInput()
		}

class SigninForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30, widget=forms.PasswordInput())
		
