from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def index(request):
    return render(request, 'pagina/index.html')

def alemania(request):
    return render(request, 'pagina/alemania.html')

def brasil(request):
    return render(request, 'pagina/brasil.html')

def argentina(request):
    return render(request, 'pagina/argentina.html')

def colocolo(request):
    return render(request, 'pagina/colocolo.html')

def cololocal(request):
    return render(request, 'pagina/cololocal.html')

def comprar(request):
    return render(request, 'pagina/comprar.html')

def madrid(request):
    return render(request, 'pagina/madrid.html')

def manchester(request):
    return render(request, 'pagina/manchester.html')

def psg(request):
    return render(request, 'pagina/psg.html')

def restodelmundo(request):
    return render(request, 'pagina/restodelmundo.html')

def selechile(request):
    return render(request, 'pagina/selechile.html')

def uchile(request):
    return render(request, 'pagina/uchile.html')

def udechilelocal(request):
    return render(request, 'pagina/udechilelocal.html')

def productoList(request):
    productos = Producto.objects.all()  
    contex = {'productos' : productos}
    return render(request, 'pagina/productoList.html', contex)

def productoAdd(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Producto agregado correctamente."
            return render(request, 'pagina/productoAdd.html', {'form': ProductoForm(), 'mensaje': mensaje})
    else:
        form = ProductoForm()
    
    return render(request, 'pagina/productoAdd.html', {'form': form})

def productoEdit(request,pk):
    producto = Producto.objects.get(id_producto=pk)
    context = {'form' : ProductoForm(instance=producto)}
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid:
            formulario.save()
            context = {'mensaje' : 'Actualización Correcta!!'}
    return render(request,'pagina/productoEdit.html', context)

def productoDel(request,pk):
    producto = Producto.objects.get(id_producto = pk) 
    producto.delete()
    return redirect(to='productoList')