from .models import Usuario, Nivel, logeados
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import usuarioSerializer, logeadosSerializer
from datetime import datetime


# Create your views here.
def formulario(request):    
    return render(request,"formulario.html")

def ingresar(request):
    ingreso = False
    rol_db = 0
    if request.GET["usuario"]:
        pasword = request.GET["pasword"]
        ingreso_usuario = request.GET["usuario"]
        user = Usuario.objects.get(usuario=ingreso_usuario)
        pasword_db = user.pasword
        rol_db = user.id_nivel
        usuario_db = user.usuario
        if pasword == pasword_db:
            ingreso = True
            l = logeados(usuario = usuario_db,
                    ingres = ingreso,
                    id_nivel = rol_db,
                    hora_log = datetime.now())
            l.save()
            context = {
                'user' : user, 
                'ingreso_usuario': ingreso_usuario,
                'pasword_db': pasword_db,
                'rol_db': rol_db,
            }
        else:
            l = logeados(usuario = usuario_db,
                    ingres = ingreso,
                    id_nivel = rol_db,
                    hora_log = datetime.now())
            l.save()
            context = {
                'user':user,
                'ingreso_usuario': ingreso_usuario,
                'pasword_db': "EL PASWORD NO COINCIDE",
                'rol_db': "No aplica"
            }
        return render(request,"ingreso.html",context) 
    else:
        mensaje = "not input"
        return HttpResponse(mensaje)



def inicio(request):
    all_users = Usuario.objects.all()
    context = {'all_users' : all_users,}
    return render(request,"inicio.html",context)

def help(request, user_id):
    return render(request,"help.html")

class usuariolist(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = usuarioSerializer

'''len(logeados)-1'''

class logeadoslist(generics.ListCreateAPIView):
    queryset = logeados.objects.filter(id=19)
    serializer_class = logeadosSerializer