from django.http import HttpResponse
from django.shortcuts import render

from account.models import Personne
from docteur.models import DossierMedical, RendezVousMedical
from hopital.models import Hopital, Service
from hopital.profilForm import ProfilHopitalForm
from hopital.serviceForm import ServiceForm

# Create your views here.


def indexHopital(request):
    h = Hopital.objects.get(idResponsable=request.user.id)
    Docteurs = Personne.objects.filter(status="docteur", hopital=h)
    Dossiers = DossierMedical.objects.all()
    RendezVousMedicalHopital = RendezVousMedical.objects.all()
    return render(request, 'hopital/indexHopital.html', {'hopital':h ,'docteurs':Docteurs,
                                                         'Dossiers':Dossiers, "RendezVousMedicalHopital":RendezVousMedicalHopital})
def profilHopital(request):
   
    if(Hopital.objects.filter(idResponsable=request.user.id).exists()):
        hopital = Hopital.objects.get(idResponsable=request.user.id)
        print("-"*100)
        return render(request, 'hopital/profilHopital.html', {'hopital':hopital})
    form = ProfilHopitalForm()
    print('-'*100)
    print(Hopital.objects.check(idResponsable=request.user.id))
    return render(request, 'hopital/suiteInscriptionHopital.html', {'form':form})
   

def updateProfilHopital(request):
    if request.method == 'POST':  
        form = ProfilHopitalForm(request.POST, request.FILES, initial={'idHopital':request.user.id }) 
        #form['idHopital'] = request.user.id 

        #print(form.data)
        if form.is_valid():  
            form = form.save(commit=False)
            form.idHopital = request.user.id 
            #print(form.data)
            form.save()
            #handle_uploaded_file(request.FILES['file'])
            return render(request, 'hopital/profilHopital.html')
        else:
            return HttpResponse("Le formulaire n'est pas valide ou le nom de l'hopital n'est pas unique. Veuiller appeler les admin")
     
    form = ProfilHopitalForm()
    return render(request, 'hopital/savefile.html', {'form': form})

def creerService(request):
    if request.method == 'POST':  
        form = ServiceForm(request.POST,  initial={'idHopital':request.user.id }) 
        #form['idHopital'] = request.user.id 

        #print(form.data)
        if form.is_valid():  
            hopital = Hopital.objects.get(idResponsable=request.user.id)
             
            form = form.save(commit=False)
            form.idHopital = request.user.id 
            form.hopital = hopital
            #print(form.data)
            form.save()
            #handle_uploaded_file(request.FILES['file'])
            ServicesHopital = Service.objects.filter(idResponsable=request.user.id)
            return render(request, 'hopital/serviceHoiptal.html',  {'ServicesHopital':ServicesHopital})
        else:
            return HttpResponse("Le formulaire n'est pas valide ou le nom de l'hopital n'est pas unique. Veuiller appeler les admin")
     
    form = ServiceForm()
    return render(request, 'hopital/creerService.html', {'form':form})

def serviceHoiptal(request):
    h = Hopital.objects.get(idResponsable=request.user.id)
    if(Service.objects.filter(hopital=h).exists()):
        ServicesHopital = Service.objects.filter(hopital=h)
        ServicesDocteurs = Personne.objects.filter(status="docteur")
        return render(request, 'hopital/serviceHoiptal.html', { 'ServicesHopital':ServicesHopital,
                                                                'ServicesDocteurs':ServicesDocteurs})
    form = ServiceForm()
    return render(request, 'hopital/creerService.html', {'form':form})
def docteurs(request):
    h = Hopital.objects.get(idResponsable=request.user.id)
    Docteurs = Personne.objects.filter(status="docteur", hopital=h)
    Dossiers = DossierMedical.objects.all()
    return render(request, "hopital/docteurs.html", {'hopital':h ,'docteurs':Docteurs, 'Dossiers':Dossiers} )

def VoirDossierMedicalHopital(request):
    h = Hopital.objects.get(idResponsable=request.user.id)
    Docteurs = Personne.objects.filter(status="docteur", hopital=h)
    Dossiers = DossierMedical.objects.all()
    return render(request, "hopital/VoirDossierMedicalHopital.html",{'hopital':h ,'docteurs':Docteurs,
                                                                     'Dossiers':Dossiers} )
