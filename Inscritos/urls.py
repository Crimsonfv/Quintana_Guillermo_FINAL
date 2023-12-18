from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('inscritos/', views.inscritos, name='Inscritos'),
    path('instituciones/', views.instituciones, name='Instituciones'),
    path('borrarInscrito/<int:inscrito_id>/', views.borrarInscrito, name='borrarInscrito'),
    path('editarInscrito/<int:inscrito_id>/', views.editarInscrito, name='editarInscrito'),
]