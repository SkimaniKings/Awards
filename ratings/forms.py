from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project,Profile



class UserReagisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
        
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title","image","user","description","link"]
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image","contact"]
    