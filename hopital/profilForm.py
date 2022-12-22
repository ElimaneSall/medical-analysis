from django import forms

from .models import  Hopital



class ProfilHopitalForm(forms.ModelForm):
    class Meta:
        model = Hopital
        fields = ['logo','nomHopital',  'adresse', 'telephone', 'email' ]
        widgets = {
            'logo': forms.FileInput(attrs={'class': 'form-control input-md', }),
            'nomHopital': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'telephone': forms.TextInput(attrs={'class': 'form-control input-md', }),
            'email': forms.EmailInput(attrs={'class': 'form-control input-md', }),
            'adresse': forms.TextInput(attrs={'class': 'form-control input-md', }),
               }