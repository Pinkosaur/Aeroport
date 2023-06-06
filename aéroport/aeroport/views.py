from django.shortcuts import render
from .forms import AvionForm
from . import models
from django.http import HttpResponseRedirect


# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = AvionForm(request)
        if form.is_valid():
            avion = form.save()
            return render(request, "aeroport/avions/affiche.html", {"avion": avion})
        else:
            return render(request, "aeroport/avions/ajout.html", {"form": form})
    else:
        form = AvionForm()
        return render(request, "aeroport/avions/ajout.html", {"form": form})


def traitement(request):
    aform = AvionForm(request.POST)
    if aform.is_valid():
        avion = aform.save()
        return render(request, "aeroport/avions/affiche.html", {"avion": avion})
    else:
        return render(request, "aeroport/avions/ajout.html", {"form": aform})


def affiche(request, id):
    avion = models.Avion.objects.get(pk=id)
    return render(request, 'aeroport/avions/affiche.html', {'avion': avion})


def update(request, id):
    avion = models.Avion.objects.get(pk=id)
    aform = AvionForm(avion.dic())
    return render(request, "aeroport/avions/ajoutupdate.html/", {"form":aform, "id":id})


def updatetraitement(request, id):
    aform = AvionForm(request.POST)
    saveid = id
    if aform.is_valid():
        avion = aform.save(commit = False)
        avion.id = saveid
        avion.save()
        return HttpResponseRedirect("/aeroport/index/")
    else:
        return render(request, "aeroport/avions/ajoutupdate.html", {"form": aform})


def delete(request, id):
    suppr = models.Avion.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/aeroport/index")


def index(request):
    liste = models.Avion.objects.all()
    return render(request, "aeroport/avions/index.html", {"liste": liste})



