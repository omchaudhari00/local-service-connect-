from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

SERVICE_TYPES = [
    ('Plumbing', 'Plumbing'),
    ('Electrical', 'Electrical'),
    ('Hardware Repair', 'Hardware Repair'),
    ('Carpentry', 'Carpentry'),
    ('Painting', 'Painting'),
    ('Other', 'Other'),
]

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, widget=forms.RadioSelect)
    phone = forms.CharField(max_length=15, required=False)
    city = forms.CharField(max_length=100, required=False)
    skill = forms.ChoiceField(choices=[('', '-- Select skill --')] + SERVICE_TYPES, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('confirm_password'):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned

class LoginForm(AuthenticationForm):
    pass
