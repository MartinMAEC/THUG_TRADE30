from django.urls import path
from django.contrib import admin
from .views import home,agregar_producto,listar_prod,modificar_prod,eliminar_prod,registro,vistaprod,admin_login_view
urlpatterns = [
    path('', home, name="home"),
    path('agregarprod/',agregar_producto,name="agregar_producto"),
    path('listarprod/',listar_prod,name="listar_prod"),
    path('modificarprod/<id>/',modificar_prod,name="modificar_prod"),
    path('eliminarprod/<id>/',eliminar_prod,name="eliminar_prod"),
    path('registro/',registro,name="registro"),
    path('vistaprod/<id>/', vistaprod, name='vistaprod'),
    path('admin-login/', admin_login_view, name='admin_login_view'),
    path('admin/', admin.site.urls),
    
]