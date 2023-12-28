from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'password1', 'password2', 'contact_number', 'birthdate', 'gender', 'profile_image']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'contact_number', 'birthdate', 'gender', 'profile_image']