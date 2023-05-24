from django.shortcuts import render
from .forms import AvionForm
from .import models
from django.http import HttpResponseRedirect

# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = AvionForm(request)
        if form.is_valid():
            avion = form.save()
            return render(request, "aeroport/affiche.html", {"avion": avion})
        else:
            return render(request, "aeroport/ajout.html", {"form": form})
    else:
        form = AvionForm()
        return render(request, "aeroport/ajout.html", {"form": form})


def traitement(request):
    aform = AvionForm(request.POST)
    if aform.is_valid():
        avion = aform.save()
        return render(request, "aeroport/affiche.html", {"avion": avion})
    else:
        return render(request, "aeroport/ajout.html", {"form": aform})


def affiche(request, id):
    avion = models.Avion.objects.get(pk=id)
    return render(request, 'aeroport/affiche.html', {'avion': avion})


def update(request, id):
    aform = AvionForm(request.POST)
    if aform.is_valid():
        avion = aform.save(commit=False)
        avion.id = id
        avion.save()
        return HttpResponseRedirect("/aeroport/affiche")
    else:
        return render(request, "aeroport/update.html", {"form": aform, "id": id})


def delete(request):
    suppr = models.Avion.objects.delete(pk=id)
    return render(request, "aeroport/index.html")


def index(request):
    liste = models.Avion.objects.all()
    return render(request,"aeroport/index.html",{"liste":liste})

