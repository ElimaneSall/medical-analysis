from django import forms

from .models import AnalyseMedicale



class AnalyseMedicaleForm(forms.ModelForm):
    class Meta:
        model = AnalyseMedicale
        fields = ['scanner', 'butAnalyse', 'patient' ]
        widgets = {
            'scanner': forms.FileInput(),
            'butAnalyse': forms.TextInput(attrs={'class': ' col-xs-6 col-sm-6 col-md-6 input-md', 'style':'border:1px solid #4ACCD1;background-color: white;color: white;'}),
            'patient': forms.TextInput(attrs={'class': 'form-control invisible', 'style':'border:2px solid #03A100;background-color: #1C00A1;color: white;'}),
            
                }