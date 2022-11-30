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
        form = AnalyseMedicaleForm(request.POST, request.FILES)  
        if form.is_valid():  
            form = form.save(commit=False)
            #form.slug = str(request.user) + str(form.nom)
            form.patient = Personne.objects.filter(matricule=request.POST.get('matricule'))[0] 
            print(form)
            form.save()
            #handle_uploaded_file(request.FILES['file'])
            AnalyseMedicalMedecin = AnalyseMedicale.objects.filter(docteur=request.user).order_by('-id')       
            return render(request, 'docteur/voirAnalyseMedicalMedecin.html', context={'AnalyseMedicalMedecin': AnalyseMedicalMedecin})
     
            #return HttpResponse("File uploaded successfuly")  
   
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

def rendezvousMedecin(request):
    RendezVousMedicalDocteur = RendezVousMedical.objects.filter(docteur=request.user).order_by('-id')
    return render(request, 'docteur/rendezvousMedecin.html',{'RendezVousMedicalDocteur':RendezVousMedicalDocteur})

   

def CreerDossierMedical(request):
    if request.method == "GET":
        if request.GET.get("pronostic") and request.GET.get("diagnostic") and request.GET.get("medicaments"):
            form = DossierMedical()
            form.pronostic = request.GET.get("pronostic")
            form.diagnostic = request.GET.get("diagnostic")
            form.medicaments = request.GET.get("medicaments")
            form.docteur = request.user
            print("-"*20)
            print(Personne.objects.filter(matricule=request.GET.get('matriculePatient')) )
            print("*"*20)
            form.patient = Personne.objects.filter(matricule=request.GET.get('matriculePatient'))[0] 
       
            # print(form['name'].value() )
            print(form)
            form.save()
                # hotel, _ = Hotel.objects.get_or_create(user=request.user)
                # hotel.chambres.add(form)
                # hotel = Hotel.objects.filter(user=request.user)
            return render(request, 'docteur/index.html')
    
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