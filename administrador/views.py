from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def menu(request):
    request.session["usuario"] = "administrador"
    usuario = request.session["usuario"]
    context = {'usuario' : usuario}
    return render(request,'administrador/menu.html', context)

def home(request):
    context={}
    return render(request,'administrador/home.html', context)

@login_required
def reporte_productos(request):
    productos = Producto.objects.all() 
    context = {'productos' : productos}
    return render(request,'administrador/menu.html', context)

def productoList(request):
    productos = Producto.objects.all()  
    contex = {'productos' : productos}
    return render(request, 'administrador/productoList.html', contex)

def productoAdd(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Producto agregado correctamente."
            return render(request, 'administrador/productoAdd.html', {'form': ProductoForm(), 'mensaje': mensaje})
    else:
        form = ProductoForm()
    
    return render(request, 'administrador/productoAdd.html', {'form': form})

def productoEdit(request,pk):
    producto = Producto.objects.get(id_producto=pk)
    context = {'form' : ProductoForm(instance=producto)}
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid:
            formulario.save()
            context = {'mensaje' : 'Actualización Correcta!!'}
    return render(request,'administrador/productoEdit.html', context)

def productoDel(request,pk):
    producto = Producto.objects.get(id_producto = pk) 
    producto.delete()
    return redirect(to='productoList')