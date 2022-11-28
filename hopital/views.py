from django.http import HttpResponse
from django.shortcuts import render

from account.models import Personne
from hopital.models import Hopital, Service
from hopital.profilForm import ProfilHopitalForm
from hopital.serviceForm import ServiceForm

# Create your views here.


def indexHopital(request):
    
    Docteurs = Personne.objects.filter(status="docteur").order_by('-id')

    totalDocteur = Docteurs.count
    return render(request, 'hopital/indexHopital.html', {'totalDocteur':totalDocteur})

# def suiteInscriptionHopital(request):
#     if request.method == "POST":
#         username = request.POST.get("nomHopital")
#         password = request.POST.get("adresse")
#         email = request.POST.get("telephone")
#         telephone = request.POST.get("logo")
        
#         if(status == "patient"):
#             user = User.objects.create_user(username=username, password=password, status=status, telephone=telephone, email=email, photoProfil=photoProfil )
#             #Patient.objects.get_or_create(adresse="Dakar")
#         else:
#             #user = User.objects.create_user(username=username, password=password , status=status, telephone=telephone, email=email)
#             user = User.objects.create_user(username=username, password=password , status=status, telephone=telephone, email=email, photoProfil=photoProfil)
#             #Docteur(specialiste="dentiste").save()
#         ## On connecte l'utilisateur
#         login(request, user)
#         ## on le redirige
#     else:
#         return(request, 'hopital/suiteInscriptionHopital.html')

def profilHopital(request):
   
    if(Hopital.objects.filter(idHopital=request.user.id).exists()):
        hopital = Hopital.objects.get(idHopital=request.user.id)
        print("-"*100)
        return render(request, 'hopital/profilHopital.html', {'hopital':hopital})
    form = ProfilHopitalForm()
    print('-'*100)
    print(Hopital.objects.check(idHopital=request.user.id))
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
            hopital = Hopital.objects.get(idHopital=request.user.id)
             
            form = form.save(commit=False)
            form.idHopital = request.user.id 
            form.hopital = hopital
            #print(form.data)
            form.save()
            #handle_uploaded_file(request.FILES['file'])
            return render(request, 'hopital/serviceHoiptal.html')
        else:
            return HttpResponse("Le formulaire n'est pas valide ou le nom de l'hopital n'est pas unique. Veuiller appeler les admin")
     
    form = ServiceForm()
    return render(request, 'hopital/creerService.html', {'form':form})

def serviceHoiptal(request):
    if(Hopital.objects.filter(idHopital=request.user.id).exists()):
        h = Hopital.objects.get(idHopital=request.user.id)
        ServicesHopital = Service.objects.filter(hopital=h)
        return render(request, 'hopital/serviceHoiptal.html', {'ServicesHopital':ServicesHopital})
    form = ServiceForm()
    return render(request, 'hopital/creerService.html', {'form':form})
