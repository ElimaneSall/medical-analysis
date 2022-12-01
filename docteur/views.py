from io import BytesIO
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views.generic import View
from account.DocteurForm import DocteurForm

from account.models import Personne
from .formAnalyseMedicale import AnalyseMedicaleForm

from .formDossierMedical import DossierMedicalForm

from .models import AnalyseMedicale, DossierMedical, RendezVousMedical

from django.template.loader import get_template
from xhtml2pdf import pisa

#Importation de keras
from django.shortcuts import render
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings 
from keras.models import load_model
model = load_model('model.h5')
#deuxieme importation
from django.shortcuts import render 
from django.core.files.storage import FileSystemStorage 
from keras.models import load_model 
from keras.preprocessing import image 
from tensorflow.keras.utils import img_to_array, load_img 

img_heigh, img_with = 150, 150 
# Create your views here.

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return HttpResponse("error")


def index(request):
    RendezVousMedicalDocteur = RendezVousMedical.objects.filter(docteur=request.user).order_by('-id')
    DossierMedicalMedecin = DossierMedical.objects.filter(docteur=request.user).order_by('-id')

    totalRV = RendezVousMedicalDocteur.count
    totalDossierMedicalMedecin = DossierMedicalMedecin.count 
    return render(request, 'docteur/index.html', {'RendezVousMedicalDocteur':RendezVousMedicalDocteur, 'totalRV':totalRV,
                             'DossierMedicalMedecin':DossierMedicalMedecin, 'totalDossierMedicalMedecin':totalDossierMedicalMedecin})

class GeneratePDF(View):
    def get(self, request, id,  *args, **kwargs):
        data = {
             'nom':'Elimane',
             'id':12,
         }
        print("*"*20)
        print(request)
        print(id)
        dossier = get_object_or_404(DossierMedical, id=id)
       
        print("-"*40)
        pdf = render_to_pdf("a.html", data)
        if pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            filename = "pdf_%s.pdf" %("ordonnance")
            content = "inline; filename =%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Page not Found")
def analyseMedicale(request):
    if request.method == 'POST':  
        form = AnalyseMedicaleForm(request.POST, request.FILES, initial={'patient':request.POST.get("matriculePatient")})  
        print(form.data)
        if form.is_valid():  
            form = form.save(commit=False)
            form.patient = Personne.objects.filter(matricule=request.POST.get('matriculePatient'))[0] 
            form.docteur = Personne.objects.filter(id=request.user.id)[0]
           
            form.save()
            #handle_uploaded_file(request.FILES['file'])
            AnalyseMedicalMedecin = AnalyseMedicale.objects.filter(docteur=request.user).order_by('-id')       
            return render(request, 'docteur/voirAnalyseMedicalMedecin.html', context={'AnalyseMedicalMedecin': AnalyseMedicalMedecin})
     
            #return HttpResponse("File uploaded successfuly")  
        else:
            return HttpResponse("Le formulaire n'est pas valide")
    form = AnalyseMedicaleForm()
    return render(request, 'docteur/analyseMedicale.html', {'form': form})

def voirAnalyseMedicalMedecin(request):
    AnalyseMedicalMedecin = AnalyseMedicale.objects.filter(docteur=request.user).order_by('-id')       
    return render(request, 'docteur/voirAnalyseMedicalMedecin.html', context={'AnalyseMedicalMedecin': AnalyseMedicalMedecin})
   

def dashboardMedecin(request):
    RendezVousMedicalDocteur = RendezVousMedical.objects.filter(docteur=request.user).order_by('-id')
    DossierMedicalMedecin = DossierMedical.objects.filter(docteur=request.user).order_by('-id')
    return render(request, 'docteur/dashboardMedecin.html',  {'RendezVousMedicalDocteur':RendezVousMedicalDocteur, 
                             'DossierMedicalMedecin':DossierMedicalMedecin,})


def CreerDossierMedical(request):
    if request.method == "GET":
        if request.GET.get("pronostic") and request.GET.get("diagnostic") and request.GET.get("medicaments"):
            form = DossierMedical()
            form.pronostic = request.GET.get("pronostic")
            form.diagnostic = request.GET.get("diagnostic")
            form.medicaments = request.GET.get("medicaments")
            form.docteur = request.user
            #form.qrCode = DossierMedical().saveQRcode()
            print("-"*20)
            print(Personne.objects.filter(matricule=request.GET.get('matriculePatient')) )
            print("*"*20)
            if Personne.objects.filter(matricule=request.GET.get('matriculePatient')).exists():
                form.patient = Personne.objects.filter(matricule=request.GET.get('matriculePatient'))[0] 
            else:
                return HttpResponse("Ce patient n'existe pas !")
            # print(form['name'].value() )
            print(form)
            form.saveQRcode()
            DossierMedicalMedecin = DossierMedical.objects.filter(docteur=request.user).order_by('-id')
            return render(request, 'docteur/index.html', {'DossierMedicalMedecin':DossierMedicalMedecin})
    
    form = DossierMedicalForm()
    return render(request, 'docteur/CreerDossierMedical.html', {'form': form})
    


def VoirDossierMedicalMedecin(request):

    DossierMedicalMedecin = DossierMedical.objects.filter(docteur=request.user).order_by('-id')

    return render(request, 'docteur/VoirDossierMedicalMedecin.html', {'DossierMedicalMedecin':DossierMedicalMedecin})


def profilDocteur(request):
    return render(request, 'docteur/profilDocteur.html')

def updateProfilDocteur(request):
    if request.method == 'POST':  
        form = DocteurForm(request.POST, request.FILES) 
        print(form.data)
        if form.is_valid():  
            user = Personne.objects.get(id=request.user.id)
            user.prenom = form.data['prenom']
            user.nom = form.data['nom']
            user.telephone = form.data['telephone']
            user.adresse = form.data['adresse']
            user.NumeroService = form.data['NumeroService']
            user.NumeroHopital = form.data['NumeroHopital']
            print("user-"*20)
            print(user.prenom)
            user.save()
            #form = form.save(commit=False)
            #form.idHopital = request.user.id 
                #print(form.data)
            #form.save()
                #handle_uploaded_file(request.FILES['file'])
            return render(request, 'docteur/profilDocteur.html')
        else:
            return HttpResponse("Le formulaire n'est pas valide ou ... Veuiller appeler les admin")
        
    return render(request, 'docteur/updateProfilDocteur.html', {'form':DocteurForm()})

def creerRendezVousPourPatient(request):
    if request.method == "GET":
        if request.GET.get("heureDebut") and request.GET.get("heureFin") and request.GET.get("objectRV"):
            form = RendezVousMedical()
            form.heureDebut = request.GET.get("heureDebut")
            form.heureFin = request.GET.get("heureFin")
            form.objectRV = request.GET.get("objectRV")
            form.docteur = request.user
            form.typeRV = request.GET.get("typeRV")
            form.dateRV = request.GET.get("dateRV")
            print("-"*20)
            print(Personne.objects.filter(matricule=request.GET.get('matriculePatient')) )
            print("*"*20)
            form.patient = Personne.objects.filter(matricule=request.GET.get('matriculePatient'))[0] 
            form.save()
            RendezVousMedicalDocteur = RendezVousMedical.objects.filter(docteur=request.user).order_by('-id')
            return render(request, 'docteur/creerRendezVousPourPatient.html', {'RendezVousMedicalDocteur':RendezVousMedicalDocteur})
    return render(request, 'docteur/creerRendezVousPourPatient.html')

def rendezvousMedecin(request):
    RendezVousMedicalDocteur = RendezVousMedical.objects.filter(docteur=request.user).order_by('-id')
    return render(request, 'docteur/rendezvousMedecin.html',{'RendezVousMedicalDocteur':RendezVousMedicalDocteur})

def IA(request):
    model = load_model('PId_Best.h5') 
labels = ['daisy','dandelion','rose', 'sunflower', 'tulip'] 
img_heigh, img_with = 150, 150 

""" ... 
    def index(): 
    You can download the entire code from this repository
    ...
""" 

def IA(request):
    context = {} 
    if request.method == 'POST': 
        
        uploaded_file= request.FILES['img'] 
        fs = FileSystemStorage() 
        name = fs.save(uploaded_file.name, uploaded_file) 
        context["url"] = fs.url(name) 
        print(context["url"]) 
        testimage = '.'+context["url"] 
        img = load_img(testimage, target_size=(img_heigh, img_with)) 
        
        x = image.img_to_array(img) 
        x = x/255 
        x = x.reshape(1, img_heigh, img_with, 3) 
        pred = model.predict(x) 
        
        import numpy as np 
        #context['predictedClass'] = labels[np.argmax(pred[0])] 
        context['probability'] = "{:.2f}".format(round(np.max(pred), 2)*100)
        
    return render(request,'docteur/ia.html',context)
    
   