from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader, RequestContext
from animal.models import Animal
from vacuna.models import Vacuna


def animal_vacuna(request, id_animal):
    object = Animal.objects.get(id=id_animal)
    vacunas = Vacuna.objects.filter(animal=object)
    template = loader.get_template('vacunas.html')
    context = RequestContext(request, {"animal": object, "vacunas": vacunas})
    return HttpResponse(template.render(context))