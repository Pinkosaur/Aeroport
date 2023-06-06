from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class AvionForm(ModelForm):
    class Meta:
        model = models.Avion
        fields = ('modele', 'comp', 'id', 'date_arrivee', 'nombre_passagers_arrivee', 'date_depart',
                  'nombre_passagers_depart')
        labels = {
            'modele': _('Modèle de l\'appareil'),
            'comp': _('Compagnie aérienne'),
            'date_arrivee': _('Date d\'entrée à l\'aéroport'),
            'nombre_passagers_arrivee': _('Nombre de passagers à l\'arrivée'),
            'date_depart': _('Date de départ de l\'aéroport'),
            'nombre_passagers_depart': _('Nombre de passagers au départ')

        }


class PersonnelForm(ModelForm):
    class Meta:
        model = models.Personnel
        fields = ('prenom', 'nom', 'metier', 'avion')
        labels = {
            'prenom': _("Prénom"),
            'nom': _("Nom"),
            'metier': _("Métier"),
            'avion': _("appareil dans lequel le personnel travaille")
        }