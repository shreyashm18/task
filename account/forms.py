'''from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    first_name=forms.CharField(max_length=50,help_text='Optional.')
    last_name=forms.CharField(max_length=50,help_text='Optional.')
    email=forms.EmailField(max_length=100,help_text='Required a valid email-address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )'''