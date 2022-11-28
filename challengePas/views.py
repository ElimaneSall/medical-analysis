from django.shortcuts import render
from django.http import HttpResponse

from account.models import Personne
from hopital.models import Service
# Create your views here.

def index(request):
    Docteurs = Personne.objects.filter(status="docteur")
    Patients = Personne.objects.filter(status="patient")
    Hopitaux = Personne.objects.filter(status="hopital")
    Services = Service.objects.all()

    # totalDocteurs = Docteurs.count
    # totalPatients = Patients.count
    # totalHopitaux = Hopitaux.count
    # totalHopitaux = Hopitaux.count
    

    return render(request, 'index.html', {'Docteurs':Docteurs, 'Patients':Patients, 'Services':Services, 'Hopitaux':Hopitaux})