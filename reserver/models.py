from django.db import models
from telnetlib import LOGOUT
#Création du model trajet
class Trajet(models.Model):
    depart = models.CharField(max_length=50)
    arrivee= models.CharField(max_length=50)
    def __str__(self):
        return self.depart+ '-' +self.arrivee
    pass


# Création du model Vol
class Vol(models.Model):
    prix = models.FloatField()
    date = models.CharField(max_length = 15 )
    heure = models.CharField(max_length = 5)
    trajet = models.ForeignKey(Trajet , on_delete = models.CASCADE)
    def __str__(self):
        return str(self.prix)+' '+ self.date +' '+ self.heure
#||||||||||||||||||||||\
#Création du Model Compagnie
class Compagnie(models.Model):
    nom = models.CharField(max_length=50)
    logo = models.ImageField()
    vols = models.ManyToManyField(Vol)
   

# Create your models here.
