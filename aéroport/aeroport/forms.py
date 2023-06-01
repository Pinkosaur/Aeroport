from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class AvionForm(ModelForm):
    class Meta:
        model = models.Avion
        fields = ('comp', 'id', 'pilote1', 'pilote2', 'date_arrivee', 'nombre_passagers_arrivee', 'date_depart',
                  'nombre_passagers_depart')
        labels = {
            'comp': _('Compagnie aérienne'),
#            'id': _('Identifiant de l\'appareil'),
            'pilote1': _('Nom du premier pilote'),
            'pilote2': _('Nom du second pilote'),
            'date_arrivee': _('Date d\'entrée à l\'aéroport'),
            'nombre_passagers_arrivee': _('Nombre de passagers à l\'arrivée'),
            'date_depart': _('Date de départ de l\'aéroport'),
            'nombre_passagers_depart': _('Nombre de passagers au départ')

        }
