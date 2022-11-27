from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect


# Create your views here.
User = get_user_model()
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        telephone = request.POST.get("phone")
        status = request.POST.get("status")
        photoProfil = request.POST.get("photoProfil")
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
        if(status == "patient"):
            return redirect('indexPatient')
        elif(status=="hopital"):
            return redirect('suiteInscriptionHopital')
        return redirect('indexDocteur')
    return render(request, 'account/signup.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def login_user(request):
    if request.method == "POST":
        #Connecter user
        username = request.POST.get("username")
        password = request.POST.get("password")
        # on check avec user dans la BD
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.status == "patient":
                return redirect('indexPatient')
            
            elif(user.status=="hopital"):
                return redirect('indexHopital')
            return redirect('indexDocteur')
    return render(request, 'account/login.html')
