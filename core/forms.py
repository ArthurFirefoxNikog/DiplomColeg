from django import forms
from .models import User
import re

class RegisterForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(min_length=3, max_length=150)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.search(r'[A-Za-z]', password):
            raise forms.ValidationError('Пароль должен содержать буквы')
        if not re.search(r'[0-9]', password):
            raise forms.ValidationError('Пароль должен содержать цифры')
        return password

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('password_confirm')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Пароли не совпадают')
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)