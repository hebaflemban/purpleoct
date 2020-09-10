from django import forms
from django.contrib.auth.models import User
from .models import Product

class LoginForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.CharField(required = True, widget = forms.PasswordInput())


class MembershipForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'password' : forms.PasswordInput(),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
