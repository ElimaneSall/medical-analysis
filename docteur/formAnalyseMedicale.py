from django import forms

from .models import AnalyseMedicale



class AnalyseMedicaleForm(forms.ModelForm):
    class Meta:
        model = AnalyseMedicale
        fields = ['scanner', 'butAnalyse', 'patient', 'docteur', 'resultat' ]
        widgets = {
            'scanner': forms.FileInput(attrs={'class': 'form-control input-md', }),
            'butAnalyse': forms.TextInput(attrs={'class':'form-control input-md'}),
            'patient': forms.TextInput(attrs={'class':'form-control input-md'}),
            
                }