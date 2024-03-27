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
