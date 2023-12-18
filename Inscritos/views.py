from django.shortcuts import render,get_object_or_404, redirect
from .models import Instituciones, Inscritos
from .forms import InscritosForm, InstitucionesForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request, 'index.html')

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

