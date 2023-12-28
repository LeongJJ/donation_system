# myapp/forms.py
from django import forms
from .models import Organizer, FundraisingEvent
from django.contrib.auth.hashers import make_password


#organizer register and login form
class OrganizerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Organizer
        fields = ['username', 'full_name', 'email', 'password', 'contact_number', 'certification_pdf']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return confirm_password
    def save(self, commit=True):
        # Hash the password before saving
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        
#fundraising event form
class FundraisingEventForm(forms.ModelForm):
    class Meta:
        model = FundraisingEvent
        fields = ['title', 'description', 'location', 'start_date', 'end_date', 'fundraising_goal']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }