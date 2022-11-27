from django.contrib import admin

# Register your models here.
from .models import DossierMedical, RendezVousMedical, AnalyseMedicale

admin.site.register(DossierMedical)
admin.site.register(RendezVousMedical)
admin.site.register(AnalyseMedicale)
