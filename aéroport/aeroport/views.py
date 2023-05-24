from django.shortcuts import render
from .forms import AvionForm
from . import models


# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = AvionForm(request)
        if form.is_valid():
            avion = form.save()
            return render(request, "/aeroport/affiche.html", {"avion": avion})
        else:
            return render(request, "aeroport/ajout.html", {"form": form})
    else:
        form = AvionForm()
        return render(request, "aeroport/ajout.html", {"form": form})


def traitement(request):
    aform = AvionForm(request.POST)
    if aform.is_valid():
        avion = aform.save()
        return render(request, "/aeroport/affiche.html", {"avion": avion})
    else:
        return render(request, "aeroport/ajout.html", {"form": aform})


def affiche(request, id):
    avion = models.Avion.objects.get(pk=id)
    return render(request, 'aeroport/affiche.html', {'avion': avion})
