from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'description', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the issue...'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. Navrangpura, Ahmedabad'}),
        }
