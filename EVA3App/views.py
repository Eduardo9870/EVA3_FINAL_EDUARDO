from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from EVA3App.forms import reservaForms

""" Para generar API """
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def index(request):
    return render(request, 'index.html')

def viewReservas(request):
    reserva = Reserva.objects.all()
    data ={
        'reserva' : reserva,
        'titulo' : 'Registro reservas'
    }
    
    return render(request, 'viewReservas.html', data)

def addReserva(request):
    data ={
        'titulo' : 'Registro reservas',
        'form' : reservaForms()
    }
    if (request.method) == 'POST':
        formulario = reservaForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/reservas')
        else:
            data['form'] = formulario
    return render(request, 'formReservas.html', data)

def deleteReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect('/reservas')

def editarReserva(request, id):
    form = Reserva.objects.get(id=id)
    data = {
        'titulo' : 'Editar reservas',
        'form' : reservaForms(instance=form)
    }
    if (request.method == 'POST'):
        form = reservaForms(request.POST, instance=form)
        if (form.is_valid()):
            form.save()
            return redirect('/reservas')
        else:
            data['form'] = form
    return render(request, 'formReservas.html', data)
    
@api_view(['GET','POST'])
def lista_reserva(request):
    if request.method == 'GET':
        """ Se obtienen todos los empleados """
        res = Reserva.objects.all()
        """ Se serializan los datos """
        serializer = ReservaSerializer(res, many=True)
        """ Se retorna la respuesta """
        return Response(serializer.data)

    if request.method == 'POST':
        """ Se serializan los datos """
        serializer = ReservaSerializer(data= request.data)
        """ Se valida la serializacion """
        if serializer.is_valid():
            """ Se guarda el registro """
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_reserva(request, id):
    try:
        res = Reserva.objects.get(id=id)
    except Reserva.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   #Obtener datos de 1 empleado
    if request.method == 'GET':
        serializer = ReservaSerializer(res)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer= ReservaSerializer(res, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    #Eliminar
    if request.method == 'DELETE':
        res.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)