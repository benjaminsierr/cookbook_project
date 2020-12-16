from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your models here.
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('first_name','last_name', 'username')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'User Name'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            
        }

    
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        help_text=("Enter the same password as above, for verification."))

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))