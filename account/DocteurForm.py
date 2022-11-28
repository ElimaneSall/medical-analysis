from django import forms

from .models import  Hopital, Personne



class DocteurForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['photoProfil','telephone', 'prenom', 'nom', 'adresse', 'hopital', 'service' ]
        widgets = {
            'photoProfil': forms.FileInput(attrs={'class': 'form-control input-md', }),
            'telephone': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'prenom': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'nom': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'adresse': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'hopital': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'service': forms.TextInput(attrs={'class': 'form-control input-md', }),
               }