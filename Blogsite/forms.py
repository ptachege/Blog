from django import forms
from .models import *

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']