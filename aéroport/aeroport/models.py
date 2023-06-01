from django.db import models


class Avion(models.Model):
    comp = models.CharField(max_length=100)
    pilote1 = models.CharField(max_length=100)
    pilote2 = models.CharField(max_length=100)
    date_arrivee = models.DateField(blank=True, null=True)
    date_depart = models.DateField(blank=True, null=True)
    nombre_passagers_depart = models.IntegerField(blank=True, null=True)
    nombre_passagers_arrivee = models.IntegerField(blank=True, null=True)

    def __str__(self):
        chaine = f"Avion de la compagnie {self.comp} piloté par {self.pilote1} et {self.pilote2}, arrivant le " \
                 f"{self.date_arrivee} avec {self.nombre_passagers_arrivee} passagers et repartant le " \
                 f"{self.date_depart} avec {self.nombre_passagers_depart} passagers"
        return chaine

    def dic(self):
        return {"comp":self.comp, "pilote1":self.pilote1, "pilote2":self.pilote2, "date_arrivee":self.date_arrivee,
                "date_depart":self.date_depart, "nombre_passagers_depart":self.nombre_passagers_depart, "nombre_passagers_arrivee":self.nombre_passagers_arrivee}


class Aeroport(models.Model):
    localisation = models.CharField(max_length=100)