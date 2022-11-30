from django.shortcuts import render
from account.models import Personne
import qrcode
from docteur.models import DossierMedical, RendezVousMedical

# Create your views here.
def indexPatient(request):
    DossierMedicalPatient = DossierMedical.objects.filter(patient=request.user).order_by('-id')
    RendezVousMedicalPatient = RendezVousMedical.objects.filter(patient=request.user).order_by('-id')

    return render(request, 'patient/index.html', {'DossierMedicalPatient':DossierMedicalPatient, 'RendezVousMedicalPatient':RendezVousMedicalPatient})

def VoirDossierMedicalPatient(request):

    DossierMedicalPatient = DossierMedical.objects.filter(patient=request.user).order_by('-id')

    return render(request, 'patient/VoirDossierMedicalPatient.html', {'DossierMedicalPatient':DossierMedicalPatient})

def rendezvousPatient(request):
    RendezVousMedicalPatient = RendezVousMedical.objects.filter(patient=request.user).order_by('-id')

    return render(request, 'patient/rendezvousPatient.html', {'RendezVousMedicalPatient':RendezVousMedicalPatient})


def creerRendezVousPatient(request):
    if request.method == "GET":
        if request.GET.get("heureDebut") and request.GET.get("heureFin") and request.GET.get("objectRV"):
            form = RendezVousMedical()
            form.heureDebut = request.GET.get("heureDebut")
            form.heureFin = request.GET.get("heureFin")
            form.objectRV = request.GET.get("objectRV")
            form.patient = request.user
            form.typeRV = request.GET.get("typeRV")
            form.dateRV = request.GET.get("dateRV")
            print("-"*20)
            print(Personne.objects.filter(matricule=request.GET.get('matriculeDocteur')) )
            print("*"*20)
            form.docteur = Personne.objects.filter(matricule=request.GET.get('matriculeDocteur'))[0] 
       
            # print(form['name'].value() )
    
            form.save()
            RendezVousMedicalPatient = RendezVousMedical.objects.filter(patient=request.user).order_by('-id')

                # hotel, _ = Hotel.objects.get_or_create(user=request.user)
                # hotel.chambres.add(form)
                # hotel = Hotel.objects.filter(user=request.user)
            return render(request, 'patient/rendezvousPatient.html', {'RendezVousMedicalPatient':RendezVousMedicalPatient})
    

    return render(request, 'patient/creerRendezVousPatient.html')

def medicamentsPatient(request):
    #Docteur = RendezVousMedical.objects.filter(docteur=request.user).order_by('-id')
    DossierMedicalPatient = DossierMedical.objects.filter(patient=request.user).order_by('-id')
    data = "Elimane Sall"
 
# Creating an instance of QRCode class
    qr = qrcode.QRCode(version = 1,
                    box_size = 10,
                    border = 5)
    
    # Adding data to the instance 'qr'
    qr.add_data(data)
    
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'red',
                        back_color = 'white')
    #totalRV = RendezVousMedicalDocteur.count
    #totalDossierMedicalMedecin = DossierMedicalMedecin.count 
    return render(request, 'patient/medicamentsPatient.html', {
                             'DossierMedicalPatient':DossierMedicalPatient, 'qrcode':img})

def ordonnancePatient(request):
     #Docteur = RendezVousMedical.objects.filter(docteur=request.user).order_by('-id')
    DossierMedicalPatient = DossierMedical.objects.filter(patient=request.user).order_by('-id')
    data = "Elimane Sall"
 
# Creating an instance of QRCode class
    qr = qrcode.QRCode(version = 1,
                    box_size = 10,
                    border = 5)
    
    # Adding data to the instance 'qr'
    qr.add_data(data)
    
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'red',
                        back_color = 'white')
    #totalRV = RendezVousMedicalDocteur.count
    #totalDossierMedicalMedecin = DossierMedicalMedecin.count 
    return render(request, 'patient/ordonnancePatient.html', {
                             'DossierMedicalPatient':DossierMedicalPatient, 'qrcode':img})

   