from django import forms
from django.core import validators
from django.forms import ModelForm
from .models import Reserva

class reservaForms(forms.Form):

    ESTADOS = [('reservado', 'RESERVADO'), ('completada', 'COMPLETADA'), ('anulada', 'ANULADA'), ('no asisten', 'NO ASISTEN')]

    nombre = forms.CharField(label='Nombre del Cliente', required=True)
    telefono = forms.IntegerField(label='Telefono del Cliente', required=True)
    fecha = forms.DateField(label='Fecha de Reserva', required=True)
    hora = forms.TimeField(label='Hora de la Reserva', required=True)
    cantidadPersonas = forms.IntegerField(label='Cantidad de personas', validators=[validators.MinValueValidator(1, 'El minimo de personas que pueden reservar es una persona'), validators.MaxValueValidator(15, 'El maximo de personas por reserva es de 15')])
    estado = forms.CharField(label= 'Estado de la reserva', widget=forms.Select(choices=ESTADOS), required=True)
    observacion = forms.CharField(label= 'Observaciones de la reservación')

class reservaForms(ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'


    ESTADOS = [('reservado', 'RESERVADO'), ('completada', 'COMPLETADA'), ('anulada', 'ANULADA'), ('no asisten', 'NO ASISTEN')]

    nombre = forms.CharField(label='Nombre del Cliente', required=True)
    telefono = forms.IntegerField(label='Telefono del Cliente', required=True)
    fecha = forms.DateField(label='Fecha de Reserva', required=True)
    hora = forms.TimeField(label='Hora de la Reserva', required=True)
    cantidadPersonas = forms.IntegerField(label='Cantidad de personas', validators=[validators.MinValueValidator(1, 'El minimo de personas que pueden reservar es una persona'), validators.MaxValueValidator(15, 'El maximo de personas por reserva es de 15')])
    estado = forms.CharField(label= 'Estado de la reserva', widget=forms.Select(choices=ESTADOS), required=True)
    observacion = forms.CharField(label= 'Observaciones de la reservación')