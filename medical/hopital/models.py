from django.db import models


# Create your models here.
class Hopital(models.Model):
    nomHopital = models.CharField(default="", max_length=50)
    adresse = models.CharField(default="", max_length=50)
    telephone = models.CharField(default="", max_length=50)
    email = models.CharField(default="", max_length=50)
    logo =models.ImageField(upload_to="logoHopital", blank=True, default=None, null=True)
    services = models.ManyToManyField("Service", verbose_name="services_hopital")
    #responsable = models.ForeignKey(Personne, on_delete=models.CASCADE, default="1", related_name="hopital_personne")
    def __str__(self):
        return self.nomHopital

class Service(models.Model):
    nomService = models.CharField(default="", max_length=50)
    chefService = models.CharField(default="", max_length=50)
    adresse = models.CharField(default="", max_length=50)
    nombreLit = models.CharField(default="", max_length=50)
    nombreLitOccupe = models.CharField(default="", max_length=50)

    def __str__(self):
        return self.nomService