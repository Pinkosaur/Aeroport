from django.db import models

class Avion(models.Model):
    modele = models.CharField(max_length=100)
    comp = models.CharField(max_length=100)
    date_arrivee = models.DateField(blank=True, null=True)
    date_depart = models.DateField(blank=True, null=True)
    nombre_passagers_depart = models.IntegerField(blank=True, null=True)
    nombre_passagers_arrivee = models.IntegerField(blank=True, null=True)
    personnel = []

    def __str__(self):
        chaine = f"{self.modele} de la compagnie {self.comp}, arrivant le " \
                 f"{self.date_arrivee} avec {self.nombre_passagers_arrivee} passagers et repartant le " \
                 f"{self.date_depart} avec {self.nombre_passagers_depart} passagers"
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
    metier = models.CharField(max_length=30, choices=CHOIX_METIER, default='1')
    avion = models.ForeignKey("avion", on_delete=models.CASCADE, default=None)
    def dic(self):
        return {"nom":self.nom, "prenom":self.prenom, "metier":self.metier, "avion":self.avion}