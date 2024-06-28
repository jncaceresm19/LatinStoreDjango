from django.shortcuts import render, redirect, get_object_or_404


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

