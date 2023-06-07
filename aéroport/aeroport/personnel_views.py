from django.shortcuts import render
from .forms import PersonnelForm
from . import models
from django.http import HttpResponseRedirect


def ajoutperso(request, id):
        form = PersonnelForm()
        models.Personnel.avion_id = id
        return render(request, "aeroport/personnel/ajoutperso.html", {"form":form, "id":id})

def traitementperso(request, id):
    avion = models.Avion.objects.get(pk=id)
    form = PersonnelForm(request.POST)
    if form.is_valid():
        personnel = form.save(commit = False) #commit = False
        personnel.avion = avion
        personnel.avion_id = id #bizarre
        personnel.save()
        return render(request, "aeroport/personnel/afficheperso.html", {"personnel": personnel, "id":id})
    else:
        return render(request, "aeroport/personnel/ajoutperso.html", {"form": form})


def afficheperso(request, id):
    personnel = models.Personnel.objects.get(pk=id)
    return render(request, 'aeroport/personnel/afficheperso.html', {'personnel': personnel, "id":id})


def updateperso(request, id):
    personnel = models.Personnel.objects.get(pk=id)
    aform = PersonnelForm(personnel.dic())
    return render(request, "aeroport/personnel/updateperso.html/", {"form":aform, "id":id, "personnel":personnel})


def updatetraitementperso(request, id):
    pers = models.Personnel.objects.get(pk=id)
    aform = PersonnelForm(request.POST)
    saveid = id
    if aform.is_valid():
        personnel = aform.save(commit = False)
        personnel.id = saveid
        personnel.avion_id = pers.avion_id
        personnel.save()
        return HttpResponseRedirect(f"/aeroport/indexperso/{pers.avion_id}")
    else:
        return render(request, "aeroport/personnel/updateperso.html", {"form": aform, "id":id})


def deleteperso(request, id):
    suppr = models.Personnel.objects.get(pk=id)
    avionid=suppr.avion_id
    suppr.delete()
    return HttpResponseRedirect(f"/aeroport/indexperso/{avionid}/")


def indexperso(request, id):
    liste = models.Personnel.objects.filter(avion_id=id)
    return render(request, "aeroport/personnel/indexperso.html", {"liste": liste, "id":id})