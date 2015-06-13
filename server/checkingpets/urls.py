from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import patterns, url
from animal.urls import urlpatterns as animal_urls
from tarea.urls import urlpatterns as tareas_urls
urlpatterns = [
    # Examples:
    # url(r'^$', 'checkingpets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'checkingpets.views.index', name='inicio'),
    url(r'^panel/', 'checkingpets.views.panel', name='panel'),

    url(r'^logout/', 'checkingpets.views.logout_view', name='logout'),
    url(r'^user/modificar/', 'checkingpets.views.modificar', name='usermod'),
    url(r'^user/modificacion/(?P<id_user>[0-9]+)', 'checkingpets.views.mod_user', name='modif'),
    url(r'^usuario_nuevo/', 'checkingpets.views.insertar_user', name='crear_user'),
    url(r'^reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/', 'checkingpets.views.reset', name='reset_confirm'),
    url(r'^password_reset/', 'checkingpets.views.reset', name='password_reset'),
    url(r'^reset/', 'checkingpets.views.envio_correo', name='reset'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += animal_urls
urlpatterns += tareas_urls