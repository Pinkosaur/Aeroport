from django.db import models

class Livre(models.Model):
    modele = models.CharField(max_length=100)
    pilote1 = models.CharField(max_length = 100)
    pilote2 = models.CharField(max_length = 100)
    date_arrivee = models.DateField(blank=True, null = True)
    date_depart = models.DateField(blank=True, null = True)
    nombre_passagers_depart = models.IntegerField(blank=True, null = True)
    nombre_passagers_arrivee = models.IntegerField(blank=True, null = True)
    id = models.IntegerField(blank=False, null=False)

    def __str__(self):
        chaine = f"{self.modele} n°{self.id} piloté par {self.pilote1} et {self.pilote2}, arrivant le " \
                 f"{self.date_arrivee} avec {self.nombre_passagers_arrivee} passagers et repartant le " \
                 f"{self.date_depart} avec {self.nombre_passagers_depart} passagers"
        return chaine

