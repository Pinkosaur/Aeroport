from django.shortcuts import render
from .forms import PersonnelForm
from . import models
from django.http import HttpResponseRedirect


def ajoutperso(request, id):
        form = PersonnelForm()
        return render(request, "aeroport/personnel/ajoutperso.html", {"form":form, "id":id})

def traitementperso(request, id):
    avion = models.Avion.objects.get(pk=id)
    form = PersonnelForm(request.POST)
    if form.is_valid():
        personnel = form.save(commit = False) #commit = False
        personnel.avion = avion
        personnel.avion_id = id #bizarre
        personnel.save()
        return render(request, "aeroport/personnel/afficheperso.html", {"personnel": personnel})
    else:
        return render(request, "aeroport/personnel/ajoutperso.html", {"form": form})


def afficheperso(request, id):
    personnel = models.Personnel.objects.get(pk=id)
    return render(request, 'aeroport/personnel/afficheperso.html', {'personnel': personnel})


def updateperso(request, id):
    personnel = models.Personnel.objects.get(pk=id)
    aform = PersonnelForm(personnel.dic())
    return render(request, "aeroport/personnel/updateperso.html/", {"form":aform, "id":id})


def updatetraitementperso(request, id):
    aform = PersonnelForm(request.POST)
    saveid = id
    if aform.is_valid():
        personnel = aform.save(commit = False)
        personnel.id = saveid
        personnel.save()
        return HttpResponseRedirect("/aeroport/indexperso/")
    else:
        return render(request, "aeroport/personnel/updateperso.html", {"form": aform})


def deleteperso(request, id):
    suppr = models.Personnel.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/aeroport/personnel/index")


def indexperso(request, id):
    liste = models.Personnel.objects.filter(pk = id)
    return render(request, "aeroport/personnel/indexperso.html", {"liste": liste, "id":id})