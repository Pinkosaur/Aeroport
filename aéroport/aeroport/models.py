import django.utils.timezone
from django.db import models

class Avion(models.Model):
    modele = models.CharField(max_length=100)
    comp = models.CharField(max_length=100)
    date_arrivee = models.DateField(default = django.utils.timezone.now())
    date_depart = models.DateField(blank=True, null=True)
    nombre_passagers_depart = models.IntegerField(default = 0)
    nombre_passagers_arrivee = models.IntegerField(default = 0)

    def __str__(self):
        if self.date_depart==None:
            depart = "à une date inconnue"
        else:
            depart = f"le {self.date_depart}"
        chaine = f"{self.modele} de la compagnie {self.comp}, arrivé le " \
                 f"{self.date_arrivee} avec {self.nombre_passagers_arrivee} passager(s) et repartant " \
                 f"{depart} avec {self.nombre_passagers_depart} passager(s)"
        return chaine

    def dic(self):
        return {"modele":self.modele, "comp":self.comp, "date_arrivee":self.date_arrivee, "date_depart":self.date_depart,
                "nombre_passagers_depart":self.nombre_passagers_depart, "nombre_passagers_arrivee":self.nombre_passagers_arrivee}



CHOIX_METIER = (
        ("Pilote", "Pilote"),
        ("Copilote", "Copilote"),
        ("Hôtesse", "Hôtesse"),
        ("Steward", "Steward"),
        ("Personnel navigant commercial", "Personnel navigant commercial"),
        ("Chef de cabine", "Chef de cabine"),
        ("Chef de cabine principal", "Chef de cabine principal"),
        ("Commandant de bord", "Commandant de bord"),
        ("Personnel navigant technique", "Personnel navigant technique"),
        ("Autre", "Autre")
         )

class Personnel(models.Model):
    nom = models.CharField(max_length=30, blank=False)
    prenom = models.CharField(max_length=30, blank=False)
    metier = models.CharField(max_length=30, choices=CHOIX_METIER, default='Hôtesse')
    avion = models.ForeignKey("avion", on_delete=models.CASCADE, default=None)
    def dic(self):
        return {"nom":self.nom, "prenom":self.prenom, "metier":self.metier, "avion":self.avion}