from . import views
from django.urls import path


urlpatterns = [
    path('', views.indexHopital, name="indexHopital"),
    path('profilHopital/', views.profilHopital, name='profilHopital'),
    path("updateProfilHopital/", views.updateProfilHopital, name="updateProfilHopital"),
    path("creerService/", views.creerService, name="creerService"),
    path("serviceHoiptal/", views.serviceHoiptal, name="serviceHoiptal"),
    path('docteursHopital', views.docteurs, name="docteursHopital"),
    path("VoirDossierMedicalHopital/", views.VoirDossierMedicalHopital, name="VoirDossierMedicalHopital"),

]