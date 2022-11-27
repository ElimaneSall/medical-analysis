from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

from hopital.models import Hopital



# Create your models here.
class Personne(AbstractUser, models.Model):
    telephone =  models.FloatField(default=10)
    status = models.CharField(max_length=200, default="user")
    matricule = models.CharField(default="0", max_length=50)
    prenom = models.CharField(default=" ", max_length=50)
    nom = models.CharField(default=" ", max_length=50)
    adresse = models.CharField(default=" ", max_length=50)
    date_naissance = models.DateTimeField(default=timezone.now)
    lieu_naissance = models.CharField(default=" ", max_length=50)
    photoProfil = models.ImageField(upload_to="users", blank=True, default=None, null=True)
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE, default=None,blank=True, null=True, related_name="docteur_hopital" )
    def __str__(self):
        return self.username
    
# class Docteur(Personne):
#     specialiste = models.CharField(max_length=200, default="user")
    


# class Patient(Personne):
#     adressse = models.CharField(max_length=200, default="user")