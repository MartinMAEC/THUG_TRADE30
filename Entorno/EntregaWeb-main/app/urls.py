from django.urls import path
from django.contrib import admin
from .views import home,agregar_producto,listar_prod,modificar_prod,eliminar_prod,registro,detalle_producto,admin_login_view,agregar_al_carrito,carrito
urlpatterns =[
    path('', home, name="home"),
    path('agregarprod/',agregar_producto,name="agregar_producto"),
    path('listarprod/',listar_prod,name="listar_prod"),
    path('modificarprod/<id>/',modificar_prod,name="modificar_prod"),
    path('eliminarprod/<id>/',eliminar_prod,name="eliminar_prod"),
    path('registro/',registro,name="registro"),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('admin-login/', admin_login_view, name='admin_login_view'),
    path('admin/', admin.site.urls),
    path('agregar-al-carrito/<int:producto_id>/',agregar_al_carrito,name='agregar_al_carrito'),
    path('carrito',carrito,name='carrito')
    
    ]