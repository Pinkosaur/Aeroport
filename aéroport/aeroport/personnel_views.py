from django.shortcuts import render
from .forms import PersonnelForm
from . import models
from django.http import HttpResponseRedirect


def ajoutperso(request):
    if request.method == "POST":
        form = PersonnelForm(request)
        if form.is_valid():
            personnel = form.save()
            return render(request, "aeroport/personnel/afficheperso.html", {"personnel": personnel})
        else:
            return render(request, "aeroport/personnel/ajoutperso.html", {"form": form})
    else:
        form = PersonnelForm()
        return render(request, "aeroport/personnel/ajoutperso.html", {"form": form})


def traitementperso(request):
    aform = PersonnelForm(request.POST)
    if aform.is_valid():
        personnel = aform.save()
        return render(request, "aeroport/personnel/afficheperso.html", {"personnel": personnel})
    else:
        return render(request, "aeroport/personnel/ajoutperso.html", {"form": aform})


def afficheperso(request, id):
    personnel = models.Personnel.objects.get(pk=id)
    return render(request, 'aeroport/personnel/afficheperso.html', {'personnel': personnel})


def updateperso(request, id):
    personnel = models.Personnel.objects.get(pk=id)
    aform = PersonnelForm(personnel.dic())
    return render(request, "aeroport/personnel/ajoutupdateperso.html/", {"form":aform, "id":id})


def updatetraitementperso(request, id):
    aform = PersonnelForm(request.POST)
    saveid = id
    if aform.is_valid():
        personnel = aform.save(commit = False)
        personnel.id = saveid
        personnel.save()
        return HttpResponseRedirect("/aeroport/indexperso/")
    else:
        return render(request, "aeroport/personnel/ajoutupdateperso.html", {"form": aform})


def deleteperso(request, id):
    suppr = models.Personnel.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/aeroport/personnel/index")


def indexperso(request):
    liste = models.Personnel.objects.all()
    return render(request, "aeroport/personnel/indexperso.html", {"liste": liste})