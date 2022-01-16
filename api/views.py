
from traceback import print_tb
from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Paciente
from .forms import PacienteForm
# Create your views here.



def inicio(request):
    return render(request, 'paginas/index.html')
def pacientes(request):    
    pacientes = Paciente.objects.all()
    return render(request, 'paginas/pacientes.html', {'pacientes': pacientes})
def crear(request):
    formulario = PacienteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('pacientes')
    return render(request, 'paginas/crear.html', {'formulario': formulario})

def actualizar(request, id):
    paciente = Paciente.objects.filter(id=id).update(estado='Atendido')
    return render(request, 'paginas/actualizar.html', {'paciente': paciente})

def ordenar(request):
    ordenadoriesgo = Paciente.objects.all().order_by('-riesgo')

    fumadorprioridad = Paciente.objects.all().filter(fuma = 'Sí', estado= 'Pendiente').order_by('-prioridad').first
    menoredad = Paciente.objects.all().filter(estado= 'Pendiente').order_by('edad').first
    mayoredad = Paciente.objects.all().filter(estado= 'Pendiente').order_by('-edad').first
    return render(request, 'paginas/pacientes.html', {'ordenadoriesgo': ordenadoriesgo, 'fumadorprioridad': fumadorprioridad, 'menoredad': menoredad, 'mayoredad': mayoredad})

def ordenarpri(request):
    ordenadopri = Paciente.objects.all().order_by('-prioridad')
    fumadorprioridad = Paciente.objects.all().filter(fuma = 'Sí', estado= 'Pendiente').order_by('-prioridad').first
    menoredad = Paciente.objects.all().filter(estado= 'Pendiente').order_by('edad').first
    mayoredad = Paciente.objects.all().filter(estado= 'Pendiente').order_by('-edad').first
    return render(request, 'paginas/ordenado.html', {'ordenadopri': ordenadopri, 'fumadorprioridad': fumadorprioridad, 'menoredad': menoredad, 'mayoredad': mayoredad})


    