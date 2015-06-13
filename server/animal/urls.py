from django.conf.urls import url

urlpatterns = [
    url(r'^animal/(?P<id_animal>[0-9]+)', 'animal.views.animal_detail', name='animal_detalle'),
    url(r'^animal/insertar', 'animal.views.insertar_animal', name='insertar_animal'),
    url(r'^animal/eliminar/(?P<id_animal>[0-9]+)', 'animal.views.borrar_animal', name='borrar_animal'),
    url(r'^animal/modificar/(?P<id_animal>[0-9]+)', 'animal.views.modificar_animal', name='animalmod'),
    ]