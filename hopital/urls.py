from . import views
from django.urls import path


urlpatterns = [
    path('', views.indexHopital, name="indexHopital"),
path("suiteInscriptionHopital/", views.suiteInscriptionHopital, name="suiteInscriptionHopital")

]