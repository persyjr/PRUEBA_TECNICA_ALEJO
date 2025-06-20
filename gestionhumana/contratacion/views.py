from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http import HttpRequest, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from . import models as m
from . import forms as f
from typing import Any
import json

# Create your views here.
class CrearCandidato(generic.CreateView):
    model = m.Candidato
    form_class = f.CandidatoForm
    template_name = 'candidato_list.html'
   
    def get_context_data(self, **kwargs):
        kwargs.update({
            'form1': self.get_form(),
            'candidatos': m.Candidato.objects.all(),
        })
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form: f.CandidatoForm) -> HttpResponse:
        estado = form.cleaned_data.get('estado')
        nombre = form.cleaned_data.get('nombre')
        cedula = form.cleaned_data.get('cedula')
        fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
        rh = form.cleaned_data.get('rh')
        ciudad_expedicion = form.cleaned_data.get('ciudad_expedicion')
        ciudad_nacimiento = form.cleaned_data.get('ciudad_nacimiento')
        ciudad_domicilio = form.cleaned_data.get('ciudad_domicilio')
        candiato = m.Candidato(
            estado=estado,
            nombre=nombre,
            cedula=cedula,
            fecha_nacimiento=fecha_nacimiento,
            rh=rh,
            ciudad_expedicion=ciudad_expedicion,
            ciudad_nacimiento=ciudad_nacimiento,
            ciudad_domicilio=ciudad_domicilio
        )
        candiato.save()

        return HttpResponseRedirect(reverse_lazy('contratacion:crear_candidato'))

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            print('CREATE')
            return self.form_valid(form)
        else:
            print('NO SE CREO')
            return self.form_invalid(form)

class EditarCandidato(generic.UpdateView):
    model = m.Candidato
    form_class = f.CandidatoForm
    template_name = 'candidato_list.html'
    
    def get_context_data(self, **kwargs):
        kwargs.update({
            'form2': self.get_form(),
            'candidatos': m.Candidato.objects.all(),
        })
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        nombre = form.cleaned_data.get('nombre')
        cedula = form.cleaned_data.get('cedula')
        fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
        rh = form.cleaned_data.get('rh')
        ciudad_expedicion = form.cleaned_data.get('ciudad_expedicion')
        ciudad_nacimiento = form.cleaned_data.get('ciudad_nacimiento')
        ciudad_domicilio = form.cleaned_data.get('ciudad_domicilio')
        candiato = m.Candidato.objects.get(pk=self.kwargs['pk'])
        candiato.nombre = nombre
        candiato.cedula = cedula
        candiato.fecha_nacimiento = fecha_nacimiento
        candiato.rh = rh
        candiato.ciudad_expedicion = ciudad_expedicion
        candiato.ciudad_nacimiento = ciudad_nacimiento
        candiato.ciudad_domicilio = ciudad_domicilio
        candiato.save()
        return HttpResponseRedirect(reverse_lazy('contratacion:crear_candidato'))

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES, instance=self.get_object())
        if form.is_valid():
            print('UPDATE')
            return self.form_valid(form)
        else:
            print('NO SE ACTUALIZO')
            return self.form_invalid(form)
        
class EliminarCandidato(generic.DeleteView):
    model = m.Candidato
    template_name = 'candidato_list.html'
    success_url = reverse_lazy('contratacion:crear_candidato')

    def get_context_data(self, **kwargs):
        kwargs.update({
            'candidatos': m.Candidato.objects.all(),
        })
        return super().get_context_data(**kwargs)

    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)
    
class CrearOferta(generic.CreateView):
    model = m.OfertaLaboral
    form_class = f.OfertaForm
    template_name = 'oferta_list.html'
   
    def get_context_data(self, **kwargs):
        kwargs.update({
            'form1': self.get_form(),
            'ofertas': m.OfertaLaboral.objects.all(),
        })
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form: f.CandidatoForm) -> HttpResponse:
        cargo = form.cleaned_data.get('cargo')
        cliente = form.cleaned_data.get('cliente')
        descripcion = form.cleaned_data.get('descripcion')
        ciudad = form.cleaned_data.get('ciudad')
        oferta = m.OfertaLaboral(
            cargo=cargo,
            cliente=cliente,
            descripcion=descripcion,
            ciudad=ciudad
        )
        oferta.save()

        return HttpResponseRedirect(reverse_lazy('contratacion:crear_oferta'))

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            print('CREATE')
            return self.form_valid(form)
        else:
            print('NO SE CREO')
            return self.form_invalid(form)


class EditarOferta(generic.UpdateView):
    model = m.OfertaLaboral
    form_class = f.OfertaForm
    template_name = 'oferta_list.html'
    
    def get_context_data(self, **kwargs):
        kwargs.update({
            'form2': self.get_form(),
            'ofertas': m.OfertaLaboral.objects.all(),
        })
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        cargo = form.cleaned_data.get('cargo')
        cliente = form.cleaned_data.get('cliente')
        descripcion = form.cleaned_data.get('descripcion')
        ciudad = form.cleaned_data.get('ciudad')
        oferta = m.OfertaLaboral.objects.get(pk=self.kwargs['pk'])
        oferta.cargo = cargo
        oferta.cliente = cliente
        oferta.descripcion = descripcion
        oferta.ciudad = ciudad
        oferta.save()
        
        return HttpResponseRedirect(reverse_lazy('contratacion:crear_oferta'))

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES, instance=self.get_object())
        if form.is_valid():
            print('UPDATE')
            return self.form_valid(form)
        else:
            print('NO SE ACTUALIZO')
            return self.form_invalid(form)

class EliminarOferta(generic.DeleteView):
    model = m.OfertaLaboral
    template_name = 'oferta_list.html'
    success_url = reverse_lazy('contratacion:crear_oferta')

    def get_context_data(self, **kwargs):
        kwargs.update({
            'ofertas': m.OfertaLaboral.objects.all(),
        })
        return super().get_context_data(**kwargs)

    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)

class CrearPostulacion(generic.CreateView):
    model = m.Postulacion
    form_class = f.PostulacionForm
    template_name = 'postulacion_list.html'
   
    def get_context_data(self, **kwargs):
        kwargs.update({
            'form1': self.get_form(),
            'postulaciones': m.Postulacion.objects.all(),
            #'leer_base' : self.leer_base()
        })
        return super().get_context_data(**kwargs)
    
    def leer_base(self,):
        print('ingreso a la base')
        with open('JSON.txt', 'r') as file:
            data = json.load(file)
            print(data)

    def form_valid(self, form: f.PostulacionForm) -> HttpResponse:
        candidato = form.cleaned_data.get('candidato')
        oferta_laboral = form.cleaned_data.get('oferta_laboral')
        postulacion = m.Postulacion(
            candidato=candidato,
            oferta_laboral=oferta_laboral
        )
        postulacion.save()

        return HttpResponseRedirect(reverse_lazy('contratacion:crear_postulacion'))

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            print('CREATE')
            return self.form_valid(form)
        else:
            print('NO SE CREO')
            return self.form_invalid(form)

class EditarPostulacion(generic.UpdateView):
    model = m.Postulacion
    form_class = f.PostulacionForm
    template_name = 'postulacion_list.html'
    
    def get_context_data(self, **kwargs):
        kwargs.update({
            'form2': self.get_form(),
            'postulaciones': m.Postulacion.objects.all(),
        })
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        candidato = form.cleaned_data.get('candidato')
        oferta_laboral = form.cleaned_data.get('oferta_laboral')
        postulacion = m.Postulacion.objects.get(pk=self.kwargs['pk'])
        postulacion.candidato = candidato
        postulacion.oferta_laboral = oferta_laboral
        postulacion.save()
        
        return HttpResponseRedirect(reverse_lazy('contratacion:crear_postulacion'))

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES, instance=self.get_object())
        if form.is_valid():
            print('UPDATE')
            return self.form_valid(form)
        else:
            print('NO SE ACTUALIZO')
            return self.form_invalid(form)

class EliminarPostulacion(generic.DeleteView):
    model = m.Postulacion
    template_name = 'postulacion_list.html'
    success_url = reverse_lazy('contratacion:crear_postulacion')

    def get_context_data(self, **kwargs):
        kwargs.update({
            'postulaciones': m.Postulacion.objects.all(),
        })
        return super().get_context_data(**kwargs)

    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)