from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.sucursal.views import sucursal_view, sucursal_list, sucursal_edit, sucursal_delete

urlpatterns = [
    
    url(r'^nuevo$', login_required(sucursal_view), name='sucursal_crear'),
    url(r'^listar$', login_required(sucursal_list), name='sucursal_listar'),
    url(r'^editar/(?P<id_sucursal>\d+)/$', login_required(sucursal_edit), name='sucursal_editar'),
    url(r'^eliminar/(?P<id_sucursal>\d+)/$', login_required(sucursal_delete), name='sucursal_eliminar'),
]