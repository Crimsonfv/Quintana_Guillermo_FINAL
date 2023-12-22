from django.urls import path
from .views import InscritosListView, InscritoDetailView
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('datos/',views.datosUser, name='index'),
    path('inscritos/', views.inscritos, name='Inscritos'),
    path('api/', views.Api, name='Api'),
    path('instituciones/', views.instituciones, name='Instituciones'),
    path('borrarInscrito/<int:inscrito_id>/', views.borrarInscrito, name='borrarInscrito'),
    path('editarInscrito/<int:inscrito_id>/', views.editarInscrito, name='editarInscrito'),
    path('api/instituciones/', views.institucionesList, name='institucionesList'),
    path('api/inscritos/', InscritosListView.as_view(), name='inscritosList'),
    path('api/inscritos/<int:id>/', InscritoDetailView.as_view(), name='inscritoDetail'),
    path('api/instituciones/<int:idInstitucion>', views.InstitucionList),
]