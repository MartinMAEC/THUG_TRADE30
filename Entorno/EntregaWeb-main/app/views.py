from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto
from .forms import ProductForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data={
        'productos': productos 
    }
    return render(request,'app/home.html',data)


def agregar_producto(request):
    data = {
        'form': ProductForm()
    }
    if request.method == 'POST':
        formulario = ProductForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()


    return render(request, 'app/producto/agregar.html', data)


def listar_prod(request):
    productos = Producto.objects.all()
    data={
        'productos' : productos
    }
    return render(request,'app/producto/listar.html',data)

def modificar_prod(request,id):
    producto = get_object_or_404(Producto, id=id)
    
    data = {
        'form' : ProductForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductForm(data=request.POST,files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_prod")
    return render(request,'app/producto/modificar.html',data)


def eliminar_prod(request,id):
    producto = get_object_or_404(Producto,id=id)
    producto.delete()
    return redirect(to="listar_prod")


def registro(request):
    data = {
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            
            content_type = ContentType.objects.get(app_label='app', model='producto')
            permission = Permission.objects.get(content_type=content_type, codename='view_producto')

            # Agregar el permiso al usuario
            user.user_permissions.add(permission)

            # Redirigir al home 
            return redirect(to="home")
            
        data["form"] = formulario
        
    return render(request, 'registration/registro.html', data)



def vistaprod(request,id):
    producto = Producto.objects.get(id=id)  # Obtén el producto deseado de la base de datos
    data = {
        'p': producto
    }
    return render(request, 'app/prod.html', data)

def admin_login_view(request):
    # Tu lógica de inicio de sesión del administrador aquí
    return render(request, 'registration/admin_login_view.html')