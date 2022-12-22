from django import forms

from .models import  Hopital, Personne



class DocteurForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['photoProfil','telephone', 'prenom', 'nom','email', 'adresse',  'NumeroService',
                  'specialite', 'bureau' , 'hopital']
        widgets = {
            'photoProfil': forms.FileInput(attrs={'class': 'form-control input-md', }),
            'telephone': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'prenom': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'nom': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'email': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'adresse': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'hopital': forms.Select(attrs={'class': 'form-control  input-md ', }),
            'NumeroService': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'specialite': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'bureau': forms.TextInput(attrs={'class': 'form-control input-md', }),
            #'hopital': forms.TextInput(attrs={'class': 'form-control input-md', }),
                    }