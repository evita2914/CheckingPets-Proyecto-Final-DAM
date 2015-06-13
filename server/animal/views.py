from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.template import loader, RequestContext
from animal.models import Animal, TipoAnimal
from animal.settings import COLORES_DICT


def animal_detail(request, id_animal):
    object = get_object_or_404(Animal, id=id_animal)
    template = loader.get_template('animal-info.html')
    context = RequestContext(request, {"animal": object, "colores": COLORES_DICT})
    return HttpResponse(template.render(context))


def insertar_animal(request):
    if request.method == "POST":
        if 'nombre' in request.POST and 'nacimiento' in request.POST:
            try:
                new_animal = Animal()
                new_animal.amo = request.user
                new_animal.nacimiento = request.POST['nacimiento']
                new_animal.nombre = request.POST['nombre']
                new_animal.descripcion = request.POST['descripcion']
                if 'color' in request.POST:
                    for codigo_color in COLORES_DICT:
                        if COLORES_DICT[codigo_color] == request.POST['color']:
                            new_animal.color = codigo_color
                if 'foto' in request.FILES:
                    new_animal.foto = request.FILES['foto']
                new_animal.tipo = TipoAnimal.objects.get(id=request.POST['tipo'])
                new_animal.save()
            except Exception as e:
                print e.message
        return redirect('panel')
    else:
        return HttpResponseBadRequest()


def borrar_animal(request, id_animal):
    object = Animal.objects.get(id=id_animal)
    object.delete()
    return redirect('panel')


def modificar_animal(request, id_animal):
    if request.method == "POST":
        if 'nom' in request.POST and 'fec' in request.POST:
            try:
                object = Animal.objects.get(id=id_animal)
                object.nombre = request.POST['nom']
                object.nacimiento = request.POST['fec']
                object.descripcion = request.POST['descrN']
                if 'color' in request.POST:
                    for codigo_color in COLORES_DICT:
                        if COLORES_DICT[codigo_color] == request.POST['color']:
                            object.color = codigo_color
                object.save()
            except Exception as e:
                print e.message
        return redirect('panel')
    else:
        return HttpResponseBadRequest()