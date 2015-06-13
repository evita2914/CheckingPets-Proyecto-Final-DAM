from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

# Create your views here.
from animal.models import Animal
from tarea.models import Tarea


def modificar_tarea(request):
    if request.method == "POST":
        import datetime
        if 'idTarea' in request.POST and 'nom' in request.POST and 'dia' in request.POST and 'hora' in request.POST and 'masc' in request.POST:
            try:
                object = Tarea.objects.get(id=request.POST['idTarea'])
                object.nombre = request.POST['nom']
                datetime_correcto = datetime.datetime.strptime(request.POST['dia'] + " " + request.POST['hora'], "%Y-%m-%d %H:%M")
                object.fecha = datetime_correcto
                object.animal = Animal.objects.get(id=request.POST['masc'])
                object.descripcion = request.POST['descrN']
                object.save()
            except Exception as e:
                print e.message
        return redirect('panel')
    else:
        return HttpResponseBadRequest()


def insertar_tarea(request):
    if request.method == "POST":
        if 'titulo' in request.POST and 'fechatarea' in request.POST:
            try:
                nueva_tarea = Tarea()
                nueva_tarea.nombre = request.POST['titulo']
                nueva_tarea.descripcion = request.POST['descripcion']
                nueva_tarea.animal_id = Animal.objects.get(id=request.POST['masc']).id
                nueva_tarea.fecha = request.POST['fechatarea'] + " " + request.POST['hora'] + ":00"
                nueva_tarea.save()
            except Exception as e:
                print e.message
        return redirect('panel')
    else:
        return HttpResponseBadRequest()

def borrar_tarea(request, id_tarea):
        nueva_tarea = Tarea.objects.filter(id=id_tarea)
        nueva_tarea.delete()
        return redirect('panel')