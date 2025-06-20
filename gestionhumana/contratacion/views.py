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
            'leer_base' : self.leer_base(),
        })
        return super().get_context_data(**kwargs)
    
    def leer_base(self,):
        print('ingreso a la base')
        with open('C:/Users/eadel/OneDrive/Documents/VISUAL_STUDIO_PROJECTS/LEARNING_PROJECTS/PRUEBA_TECNICA_ALEJO/JSON.txt', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)
            # convertir a lista de objetos Candidato
            candidatos = []
            for item in data:
                candidato = m.Candidato(
                    estado='Reclutamiento',
                    nombre=item.get('nombre'),
                    cedula=item.get('doctO_IDENT'),
                    rh=item.get('grupO_RH'),
                    ciudad_expedicion=item.get('ciudad_e'),
                    ciudad_nacimiento=item.get('ciudad_n'),
                    ciudad_domicilio=item.get('ciudad_d')
                )
                candidato.save()

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
            
        })
        return super().get_context_data(**kwargs)
    
    

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
    
class CrearOrdenDeContratacion(generic.CreateView):
    model = m.OrdenDeContratacion
    form_class = f.OrdenDeContratacionForm
    template_name = 'ordenes_list.html'
    # success_url no está definido aquí en el código que me muestras. ESTO ES CLAVE.

    def get_context_data(self, **kwargs):
        kwargs.update({
            'ordenes': m.OrdenDeContratacion.objects.all(),
            'form1': self.get_form(),
        })
        return super().get_context_data(**kwargs)
    def form_valid(self, form: f.OrdenDeContratacionForm) -> JsonResponse:
        # Esto guardará el objeto y lo asignará a self.object
        self.object = form.save()
        # En caso de éxito, respondemos con JSON y estado 200
        return JsonResponse({'success': True, 'message': 'Orden de Contratación creada exitosamente.'}, status=200)
    
    def form_valid(self, form: f.OrdenDeContratacionForm) -> HttpResponse:
        # Aquí estás creando y guardando el objeto manualmente
        orden = m.OrdenDeContratacion(
            postulacion=form.cleaned_data.get('postulacion'),
            cliente=form.cleaned_data.get('cliente'),
            cargo=form.cleaned_data.get('cargo'),
            examenes=form.cleaned_data.get('examenes')
        )
        orden.save()

        # Y aquí estás redirigiendo manualmente
        return HttpResponseRedirect(reverse_lazy('contratacion:crear_orden'))

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            print('CREATE')
            return self.form_valid(form) # Llama a tu form_valid personalizado
        else:
            print('NO SE CREO')
            return JsonResponse({'success': True, 'message': 'Usuario ya tiene Postulacion en proceso'}, status=200)
            return self.form_invalid(form) # Llama a form_invalid

class EditarOrdenDeContratacion(generic.UpdateView):
    model = m.OrdenDeContratacion
    form_class = f.OrdenDeContratacionForm
    template_name = 'ordenes_list.html'
    
    def get_context_data(self, **kwargs):
        kwargs.update({
            'form2': self.get_form(),
            'ordenes': m.OrdenDeContratacion.objects.all(),
        })
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        orden = m.OrdenDeContratacion.objects.get(pk=self.kwargs['pk'])
        orden.postulacion = form.cleaned_data.get('postulacion')
        orden.cliente = form.cleaned_data.get('cliente')
        orden.cargo = form.cleaned_data.get('cargo')
        orden.examenes = form.cleaned_data.get('examenes')
        orden.save()
        
        return HttpResponseRedirect(reverse_lazy('contratacion:crear_orden'))

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES, instance=self.get_object())
        if form.is_valid():
            print('UPDATE')
            return self.form_valid(form)
        else:
            print('NO SE ACTUALIZO')
            return self.form_invalid(form)
        
class EliminarOrdenDeContratacion(generic.DeleteView):
    model = m.OrdenDeContratacion
    template_name = 'ordenes_list.html'
    success_url = reverse_lazy('contratacion:crear_orden')

    def get_context_data(self, **kwargs):
        kwargs.update({
            'ordenes': m.OrdenDeContratacion.objects.all(),
        })
        return super().get_context_data(**kwargs)

    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)