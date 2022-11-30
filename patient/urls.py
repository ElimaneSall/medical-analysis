from . import views
from django.urls import path


urlpatterns = [
    path('', views.indexPatient, name="indexPatient"),
    path('VoirDossierMedicalPatient/', views.VoirDossierMedicalPatient, name="VoirDossierMedicalPatient"),
    path("rendezvousPatient/", views.rendezvousPatient, name="rendezvousPatient"),
    path("creerRendezVousPatient/", views.creerRendezVousPatient, name="creerRendezVousPatient"),
    path("medicamentsPatient", views.medicamentsPatient, name="medicamentsPatient"),
    path("ordonnancePatient/", views.ordonnancePatient, name="ordonnancePatient")
]