from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'image',
            'file'
        ]


class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'image',
            'file'
        ]


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',
                  'password1',
                  'password2')


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
