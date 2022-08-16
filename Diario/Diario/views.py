from django.shortcuts import render
from AppDiario.forms import *
from AppDiario.models import *



def inicio(request):
    if request.user.is_authenticated:
        imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppDiario/inicio.html",{"imagen":imagen})
    else:
        return render(request, "AppDiario/inicio.html")