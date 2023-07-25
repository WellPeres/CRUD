from django.contrib import admin
from django.urls import path, include
from . views import index, home, salvar, editar, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('estudos/', home, name='home'),
    path('estudos/salvar', salvar, name='salvar'),
    path('estudos/editar/<int:id>', editar, name='editar'),
    path('estudos/update/<int:id>', update, name='update'),
    path('estudos/delete/<int:id>', delete, name='delete'),
]
