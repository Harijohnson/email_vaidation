# from django.forms import ModelForm
# from django.forms.widgets import PasswordInput
from .models import User

# class UserModelForm(ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             "email",
#             'password1',
#             'password2',
#             ]

# authentication/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)



class UserModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class PasswordChangeModelForm(PasswordChangeForm):
    class Meta:
        model = User

class LoginUser(forms.Form):
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'password1']