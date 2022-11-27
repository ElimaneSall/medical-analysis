from django.shortcuts import render

from account.models import Personne

# Create your views here.


def indexHopital(request):
    
    Docteurs = Personne.objects.filter(status="docteur").order_by('-id')

    totalDocteur = Docteurs.count
    return render(request, 'hopital/indexHopital.html', {'totalDocteur':totalDocteur})

def suiteInscriptionHopital(request):
    if request.method == "POST":
        username = request.POST.get("nomHopital")
        password = request.POST.get("adresse")
        email = request.POST.get("telephone")
        telephone = request.POST.get("logo")
        
        if(status == "patient"):
            user = User.objects.create_user(username=username, password=password, status=status, telephone=telephone, email=email, photoProfil=photoProfil )
            #Patient.objects.get_or_create(adresse="Dakar")
        else:
            #user = User.objects.create_user(username=username, password=password , status=status, telephone=telephone, email=email)
            user = User.objects.create_user(username=username, password=password , status=status, telephone=telephone, email=email, photoProfil=photoProfil)
            #Docteur(specialiste="dentiste").save()
        ## On connecte l'utilisateur
        login(request, user)
        ## on le redirige
    else:
        return(request, 'hopital/suiteInscriptionHopital.html')