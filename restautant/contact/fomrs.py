
from django import forms
from .models import Contact 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  
        fields = ['name', 'email', 'message']  # Define the fields you want to include


