from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import CustomUser


class SignUpForm(UserCreationForm):

    password1 = forms.CharField(label="Password",
                               widget = forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Password"}))
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Confirm Password"}))
    full_name = forms.CharField(label="Full name*",
                                widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Full Name"}))
    phone_number = forms.CharField(label="Phone Number*",
                                widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}))

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'username', 'phone_number', 'password1', 'password2']

        widgets = {
            'username':forms.TextInput(attrs={"class":"form-control", "placeholder":"username"}),
            'email': forms.EmailInput(attrs={"class":"form-control", "placeholder":"Email"}),
        }