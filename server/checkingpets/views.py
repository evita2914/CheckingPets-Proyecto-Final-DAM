# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm

from animal.forms import FotoAnimalForm
from animal.models import Animal, TipoAnimal
from animal.settings import COLORES_DICT
from tarea.models import Tarea


def index(request):
    if request.user.is_authenticated():
        return redirect('panel')

    datos = {'error': False}

    if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if len(username) == 0:
            error_msg = "Falta el usuario ;)"
        elif len(password) == 0:
            error_msg = "Falta la contraseña!!"
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('panel')
                else:
                    error_msg = "Tu cuenta no está activada, contacta con el administrador"
            else:
                error_msg = "Login incorrecto"
        datos["error_msg"] = error_msg
        datos["error"] = True

    template = loader.get_template('index.html')
    context = RequestContext(request, datos)
    return HttpResponse(template.render(context))


@login_required
def panel(request):
    animales = Animal.objects.filter(amo=request.user)
    tareas = Tarea.objects.filter(animal__in=animales).order_by('fecha')
    tipos = TipoAnimal.objects.all()
    formset = FotoAnimalForm()
    template = loader.get_template('panel.html')
    context = RequestContext(request,
                             {"animales": animales, "tareas": tareas, "tiposanimal": tipos, "fotoform": formset,
                              "colores": COLORES_DICT})
    return HttpResponse(template.render(context))


def logout_view(request):
    logout(request)
    template = loader.get_template('logout.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def reset_confirm(request, uidb36=None, token=None):
    return password_reset_confirm(request, template_name='reset_confirm.html',
                                  uidb36=uidb36, token=token, post_reset_redirect=reverse('checkingpets:index'))


def reset(request):
    return password_reset(request, template_name='password_reset.html',
                          email_template_name='reset_email.html',
                          subject_template_name='password_reset_subject.txt',
                          post_reset_redirect='/')


def insertar_user(request):
    from django.contrib.auth.models import User

    if request.method == "POST":
        if 'user' in request.POST and 'passwd' in request.POST:
            try:
                user = User.objects.create_user(
                    email=request.POST['email'],
                    first_name=request.POST['firstname'],
                    last_name=request.POST['lastname'],
                    username=request.POST['user'],
                    password=request.POST['passwd'])
            except Exception as e:
                print e.message
            return redirect('inicio')
        else:
            return HttpResponseBadRequest()


def envio_correo(request):
    from django.core.mail import send_mail
    from django.contrib.auth.hashers import make_password
    import smtplib

    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.starttls()
    smtp.login('checkingpets@gmail.com', 'ismayeva')
    if request.method == "POST":
        if 'email' in request.POST and 'user' in request.POST:
            try:
                datos = {'error': False}
                usuario = request.POST['user']
                parte1 = request.POST['email']
                partes = parte1.partition("@")
                parteprim = partes[0]
                mensaje = "Tus datos de entrada al correo son...\nUsuario: " + usuario
                mensaje2 = "Pass: " + parteprim + usuario
                send_mail("Contraseña nueva",
                          mensaje + "\n" + mensaje2,
                          '<checkingpets@gmail.com>',
                          [request.POST['email']],
                          fail_silently=False)
                objeto = User.objects.get(username=usuario)
                objeto.password = make_password(parteprim + usuario)
                objeto.save()

            except Exception as e:
                print e.message
            return redirect('inicio')
        else:
            return HttpResponseBadRequest()

def modificar(request):
    template = loader.get_template('modificar.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def mod_user(request, id_user):
    from django.contrib.auth.models import User
    from django.contrib.auth.hashers import make_password
    if request.method == "POST":
        if 'user' in request.POST and 'passwd' in request.POST:
            try:
                user = User.objects.get(id=id_user)
                if request.POST['email'] != '':
                    user.email=request.POST['email']
                if request.POST['user'] != '':
                    user.username=request.POST['user']
                if request.POST['passwd'] != '':
                    user.password=make_password(request.POST['passwd'])
                user.save()
            except Exception as e:
                    print e.message
            return redirect('panel')
        else:
            return redirect('panel')