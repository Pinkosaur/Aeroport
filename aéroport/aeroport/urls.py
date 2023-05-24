from django.urls import path
from . import views

urlpatterns = [
    path('ajout/', views.ajout),
    path('traitement', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete),
    path('index/', views.index),
]
