from http.client import responses
from django.shortcuts import render,get_object_or_404, redirect
from .models import Instituciones, Inscritos
from .forms import InscritosForm, InstitucionesForm
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .serializers import InscritosSerializer, InstitucionesSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


def index(request):
    return render(request, 'index.html')

def Api(request):
    return render(request, 'API.html')

def datosUser(request):
    data = {
        'nombres': 'Guillermo Joaquin',
        'apellidos': 'Quintana Arriagada',
        'rut': '20366060-k',
        'seccion': '(TI2041/IEI-170-N4/D Temuco IEI)'
    }
    return JsonResponse(data)

def inscritos(request):
    if request.method == 'POST':
        form = InscritosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Inscritos'))
    else:
        form = InscritosForm()
    inscritos = Inscritos.objects.all()
    return render(request, 'inscritos.html', {'inscritos': inscritos, 'form': form})

def borrarInscrito(request, inscrito_id):
    inscrito = get_object_or_404(Inscritos, id=inscrito_id)
    inscrito.delete()
    return redirect('Inscritos')

def editarInscrito(request, inscrito_id):
    inscrito = get_object_or_404(Inscritos, id=inscrito_id)
    if request.method == 'POST':
        form = InscritosForm(request.POST, instance=inscrito)
        if form.is_valid():
            form.save()
            return redirect('Inscritos')
    else:
        form = InscritosForm(instance=inscrito)
    return render(request, 'editarInscrito.html', {'form': form})

def instituciones(request):
    if request.method == 'POST':
        form = InstitucionesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Instituciones'))
    else:
        form = InstitucionesForm()

    instituciones = Instituciones.objects.all()
    return render(request, 'instituciones.html', {'instituciones': instituciones, 'form': form})

#Inscritos usando una clase

class InscritosListView(APIView):
    def get(self, request):
        inscritos = Inscritos.objects.all()
        serializer = InscritosSerializer(inscritos, many=True)
        return Response(serializer.data)

class InscritoDetailView(APIView):
    def get_object(self, id):
        try:
            return Inscritos.objects.get(id=id)
        except Inscritos.DoesNotExist:
            raise Http404

    def get(self, request, id):
        inscrito = self.get_object(id)
        serializer = InscritosSerializer(inscrito)
        return Response(serializer.data)


#institucion usando funcion
@api_view(['GET', 'POST'])
def institucionesList(request):
    if request.method == 'GET':
        instituciones = Instituciones.objects.all()
        serializer = InstitucionesSerializer(instituciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InstitucionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def InstitucionList(request, idInstitucion):

    try:
        institucion = Instituciones.objects.get(id=idInstitucion)
    except institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = InstitucionesSerializer(institucion)
        return Response(serial.data)