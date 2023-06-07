from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import maquinaria, codigos_demora, turnaround, usuario, aerolinea, plantilla, vuelo
import json

# Create your views here.

class MaquinariaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        maquinarias = list(maquinaria.objects.values())
        if len(maquinarias)>0:
            datos={'mensaje':'Success','maquinarias':maquinarias}
        else:
            datos={'mensaje':'No hay maquinarias'}
        return JsonResponse(datos)

    def post(self, request):
        jsondata = json.loads(request.body)
        maquinaria.objects.create(identificador=jsondata['identificador'], modelo=jsondata['modelo'], combustible=jsondata['combustible'], estado=jsondata['estado'], categoria=jsondata['categoria'] ,imagen=jsondata['imagen'])
        datos={'mensaje':'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jsondata = json.loads(request.body)
        maquinarias = list(maquinaria.objects.filter(id=id).values())
        if len(maquinarias)>0:
            maquina = maquinaria.objects.get(id=id)
            maquina.identificador = jsondata['identificador']
            maquina.modelo = jsondata['modelo']
            maquina.combustible = jsondata['combustible']
            maquina.estado = jsondata['estado']
            maquina.categoria = jsondata['categoria']
            maquina.imagen = jsondata['imagen']
            maquina.save()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No hay maquinarias'}
        return JsonResponse(datos)

    def delete(self, request, id):
        maquinarias = list(maquinaria.objects.filter(id=id).values())
        if len(maquinarias)>0:
            maquinaria.objects.filter(id=id).delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No hay maquinarias'}
        return JsonResponse(datos)
    

class CodigoDemoraView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        codigo = list(codigos_demora.objects.values())
        if len(codigo)>0:
            datos={'mensaje':'Success','codigoss':codigo}
        else:
            datos={'mensaje':'No hay codigos'}
        return JsonResponse(datos)
    

class TurnaroundView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        turnarounds = list(turnaround.objects.values())
        if len(turnarounds)>0:
            datos={'mensaje':'Success','turnarounds':turnarounds}
        else:
            datos={'mensaje':'No hay turnarounds'}
        return JsonResponse(datos)
    
class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        usuarios = list(usuario.objects.values())
        if len(usuarios)>0:
            datos={'mensaje':'Success','usuarios':usuarios}
        else:
            datos={'mensaje':'No hay usuarios'}
        return JsonResponse(datos)
    
    def post(self, request):
        jsondata = json.loads(request.body)
        usuario.objects.create(cedula=jsondata['cedula'], cargo=jsondata['cargo'], departameto=jsondata['departamento'], correo=jsondata['correo'], telefono=jsondata['telefono'], turno=jsondata['turno'] ,contrasena=jsondata['contrasena'], estado=jsondata['estado'] ,imagen=jsondata['imagen'])
        datos={'mensaje':'Success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jsondata = json.loads(request.body)
        usuarios = list(usuario.objects.filter(id=id).values())
        if len(usuarios)>0:
            user = usuario.objects.get(id=id)
            user.cedula = jsondata['cedula']
            user.cargo = jsondata['cargo']
            user.departameto = jsondata['departamento']
            user.correo = jsondata['correo']
            user.telefono = jsondata['telefono']
            user.turno = jsondata['turno']
            user.contrasena = jsondata['contrasena']
            user.estado = jsondata['estado']
            user.imagen = jsondata['imagen']
            user.save()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe el usuario'}
        return JsonResponse(datos) 
    
    def delete(self, request, id):
        usuarios = list(usuario.objects.filter(id=id).values())
        if len(usuarios)>0:
            usuario.objects.filter(id=id).delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe ese usuario'}
        return JsonResponse(datos)
    

class AerolineaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        aerolineas = list(aerolinea.objects.values())
        if len(aerolineas)>0:
            datos={'mensaje':'Success','aerolineas':aerolineas}
        else:
            datos={'mensaje':'No hay aerolineas'}
        return JsonResponse(datos)
    
    def post(self, request):
        jsondata = json.loads(request.body)
        aerolinea.objects.create(nombre=jsondata['nombre'], correo=jsondata['correo'], telefono=jsondata['telefono'], codigo=jsondata['codigo'], imagen=jsondata['imagen'])
        datos={'mensaje':'Success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jsondata = json.loads(request.body)
        aerolineas = list(aerolinea.objects.filter(id=id).values())
        if len(aerolineas)>0:
            user = aerolinea.objects.get(id=id)
            user.nombre = jsondata['nombre']
            user.correo = jsondata['correo']
            user.telefono=jsondata['telefono']
            user.codigo=jsondata['codigo']
            user.imagen = jsondata['imagen']
            user.save()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la aerolinea'}
        return JsonResponse(datos) 
    
    def delete(self, request, id):
        aerolineas = list(aerolinea.objects.filter(id=id).values())
        if len(aerolineas)>0:
            aerolinea.objects.filter(id=id).delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la aerolinea'}
        return JsonResponse(datos)

class PlantillaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        plantillas = list(plantilla.objects.values())
        if len(plantillas)>0:
            datos={'mensaje':'Success','plantillas':plantillas}
        else:
            datos={'mensaje':'No hay plantillas'}
        return JsonResponse(datos)
    
    def post(self, request):
        jsondata = json.loads(request.body)
        plantilla.objects.create(titulo=jsondata['titulo'])
        datos={'mensaje':'Success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jsondata = json.loads(request.body)
        plantillas = list(plantilla.objects.filter(id=id).values())
        if len(plantillas)>0:
            user = plantilla.objects.get(id=id)
            user.titulo = jsondata['titulo']
            user.save()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la plantilla'}
        return JsonResponse(datos) 
    
    def delete(self, request, id):
        plantillas = list(plantilla.objects.filter(id=id).values())
        if len(plantillas)>0:
            plantilla.objects.filter(id=id).delete()
            datos={'mensaje':'Success'}
        else:
            datos={'mensaje':'No existe la plantilla'}
        return JsonResponse(datos)
    

class VueloView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        vuelos = list(vuelo.objects.values())
        if len(vuelos)>0:
            datos={'mensaje':'Success','vuelos':vuelos}
        else:
            datos={'mensaje':'No hay vuelos'}
        return JsonResponse(datos)
    