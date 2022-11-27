from django import forms

from .models import DossierMedical



class DossierMedicalForm(forms.ModelForm):
    class Meta:
        model = DossierMedical
        fields = ['patient', 'pronostic', 'diagnostic', 'medicaments', ]
        widgets = {
            'patient': forms.TextInput(attrs={'class': 'form-control', 'style':'border:2px solid #03A100;background-color: #1C00A1;color: white;'}),
            'pronostic': forms.TextInput(attrs={'class': 'form-control', 'style':'border:2px solid #03A100;background-color: #1C00A1;color: white;'}),
            'diagnostic': forms.TextInput(attrs={'class': 'form-control', 'style':'border:2px solid #03A100;background-color: #1C00A1;color: white;'}),
            'medicaments': forms.TextInput(attrs={'class': 'form-control', 'style':'border:2px solid #03A100;background-color: #1C00A1;color: white;'}),
                 }