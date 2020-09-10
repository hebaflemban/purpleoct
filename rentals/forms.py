from django import forms
from django.contrib.auth.models import User
from .models import Product


class LoginForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.CharField(required = True, widget = forms.PasswordInput())

# class searchForm(forms.Form):
#     category

class MembershipForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProductRent(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_rented']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
