from django.urls import path
from . import views, personnel_views

urlpatterns = [
    path('ajout/', views.ajout),
    path('traitement', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),
    path('index/', views.index),

    path('ajoutperso/', personnel_views.ajoutperso),
    path('traitementperso', personnel_views.traitementperso),
    path('afficheperso/<int:id>/', personnel_views.afficheperso),
    path('updateperso/<int:id>/', personnel_views.updateperso),
    path('updatetraitementperso/<int:id>/', personnel_views.updatetraitementperso),
    path('deleteperso/<int:id>/', personnel_views.deleteperso),
    path('indexperso/', personnel_views.indexperso),
]
