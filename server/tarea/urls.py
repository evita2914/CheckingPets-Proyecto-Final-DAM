from django.conf.urls import url

urlpatterns = [
    url(r'^tarea/insertar', 'tarea.views.insertar_tarea', name='insertar_tarea'),
    url(r'^tarea/modificar', 'tarea.views.modificar_tarea', name='tareamod'),
    url(r'^tarea/borrar/(?P<id_tarea>[0-9]+)', 'tarea.views.borrar_tarea', name='bortar'),
    ]