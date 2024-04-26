from django import forms
from .models import Profile

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email =forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput,)
    password2= forms.CharField(widget=forms.PasswordInput,label='confirm password ')


class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['firstname','lastname','location','bio','pic']



