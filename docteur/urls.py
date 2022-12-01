from . import views
from django.urls import path
from .views import GeneratePDF

urlpatterns = [
    path('', views.index, name="indexDocteur"),
    path('creerDossierMedical', views.CreerDossierMedical, name="CreerDossierMedical"),
    path('analyseMedicale', views.analyseMedicale, name="analyseMedicale"),
    path('dashboardMedecin', views.dashboardMedecin, name="dashboardMedecin"),
    path('rendezvousMedecin', views.rendezvousMedecin, name="rendezvousMedecin"),
    path("VoirDossierMedicalMedecin", views.VoirDossierMedicalMedecin, name="VoirDossierMedicalMedecin"),
    path("voirAnalyseMedicalMedecin",views.voirAnalyseMedicalMedecin , name="voirAnalyseMedicalMedecin"),
    path("pdf/<str:id>/", GeneratePDF.as_view(), name="pdf"),
    path("profilDocteur/", views.profilDocteur, name="profilDocteur"),
    path("updateProfilDocteur/",views.updateProfilDocteur, name="updateProfilDocteur"),
    path("creerRendezVousPourPatient/", views.creerRendezVousPourPatient, name="creerRendezVousPourPatient"),
    path("IA/", views.IA, name="IA")

]