import random
from django.utils import timezone
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

from account.models import Personne
# Create your models here.

class DossierMedical(models.Model):
    pronostic = models.CharField(max_length=100, default="")
    diagnostic = models.CharField(max_length=200, default="")
    medicaments = models.TextField(default="")
    statut = models.TextField(default="en cours", null=True, blank=True)
    docteur = models.ForeignKey(Personne, on_delete=models.CASCADE, default="1", related_name="docteur_dossiermedical")
    patient = models.ForeignKey(Personne, on_delete=models.CASCADE, default="1", related_name="DossierMedical_patient")
    date_creationDossierMedical= models.DateTimeField(default=timezone.now)
    qrCode = models.ImageField(upload_to="qrCode", blank=True, null=True, default=None)
    def __str__(self):
        return str(self.docteur) + " " + str(self.patient)
    
    def saveQRcode(self, *args, **kwargs):
        data = 'http://www.alloDocteur/docteur/pdf/24/'
        img = qrcode.make(data)
        canvas = Image.new('RGB', (290, 290), '#20c997')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(img)
        fname = f'qr_code_{self.id}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qrCode.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
   

class RendezVousMedical(models.Model):
    date_priseRV = models.DateTimeField(default=timezone.now)
    date_RV = models.DateField(default=timezone.now)
    heureDebut = models.CharField(default="10h00", max_length=50)
    heureFin = models.CharField( default="12h00", max_length=50)
    typeRV = models.CharField(default="", max_length=200)
    objectRV = models.TextField(default="")
    statut = models.TextField(default="non confirmé")
    docteur = models.ForeignKey(Personne, on_delete=models.CASCADE, default="1", related_name="docteur_rendezvousmedical")
    patient = models.ForeignKey(Personne, on_delete=models.CASCADE, default="1", related_name="patient_rendezvousmedical")

    def __str__(self):
        return str(self.docteur) + " " + str(self.patient)

class AnalyseMedicale(models.Model):
    scanner =  models.ImageField(upload_to="users", blank=True, default=None, null=True)
    butAnalyse = models.TextField(default=" ")
    resultat = models.CharField(max_length=200, default="Paludisme", null=True, blank=True)
    observation = models.TextField(default=" ")
    dateAnalyse = models.DateTimeField(default=timezone.now)
    docteur = models.ForeignKey(Personne, on_delete=models.CASCADE, default="1", related_name="docteur_analysemedical")
    patient = models.ForeignKey(Personne, on_delete=models.CASCADE, default="1", related_name="AnalyseMedical_patient")
    #date_creationDossierMedical= models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.docteur) + " " + str(self.patient)