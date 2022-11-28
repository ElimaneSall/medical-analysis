from django import forms

from .models import  Service



class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['nomService','chefService', 'adresse', 'nombreLit', 'nombreLitOccupe', 'hopital' ]
        widgets = {
            'nomService': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'chefService': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'nombreLit': forms.NumberInput(attrs={'class': 'form-control input-md', }),
            'nombreLitOccupe': forms.NumberInput(attrs={'class': 'form-control input-md', }),
            'adresse': forms.TextInput(attrs={'class': 'form-control input-md', }),
               }