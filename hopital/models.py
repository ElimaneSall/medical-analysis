from django.db import models


# Create your models here.
class Hopital(models.Model):
    nomHopital = models.CharField(default="", max_length=50, unique=True)
    adresse = models.CharField(default="", max_length=50)
    telephone = models.CharField(default="", max_length=50)
    email = models.CharField(default="", max_length=50)
    idResponsable = models.CharField(default="", max_length=50)
    logo =models.ImageField(upload_to="logoHopital", blank=True, default=None, null=True)
    #services = models.ManyToManyField("Service", verbose_name="services_hopital")
    idHopital =models.CharField(default="", max_length=50,unique=True)
    #responsable = models.ForeignKey(Personne, on_delete=models.CASCADE, default="1", related_name="hopital_personne")
    def __str__(self):
        return self.nomHopital + str(self.idHopital)
   

class Service(models.Model):
    nomService = models.CharField(default="", max_length=50)
    idService = models.CharField(default="", max_length=50)
    idResponsable = models.CharField(default="", max_length=50)
    chefService = models.CharField(default="", max_length=50)
    adresse = models.CharField(default="", max_length=50)
    nombreLit = models.IntegerField(default=0)
    nombreLitOccupe = models.IntegerField(default=0)
    hopital = models.ForeignKey(Hopital, verbose_name="hopital_service", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nomService