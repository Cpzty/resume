from django import forms
from . models import ContactProfile

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
                'placeholder': '*Full name..',
                'class' : 'form-control'
                }))
    