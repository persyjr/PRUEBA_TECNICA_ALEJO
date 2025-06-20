from django.contrib import admin
from . import models as m

# Register your models here.
@admin.register(m.Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula', 'estado', 'fecha_nacimiento', 'rh', 'ciudad_expedicion', 'ciudad_nacimiento', 'ciudad_domicilio')
    search_fields = ('nombre', 'cedula')
    list_filter = ('ciudad_expedicion', 'ciudad_nacimiento', 'ciudad_domicilio')

@admin.register(m.OfertaLaboral)
class OfertaLaboralAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'cliente', 'ciudad')
    search_fields = ('cargo', 'cliente')
    list_filter = ('ciudad',)

@admin.register(m.Postulacion)
class PostulacionAdmin(admin.ModelAdmin):
    list_display = ('candidato', 'oferta_laboral')
    search_fields = ('candidato__nombre', 'oferta_laboral__cargo')
    list_filter = ('oferta_laboral__ciudad',)

@admin.register(m.OrdenDeContratacion)
class OrdenDeContratacionAdmin(admin.ModelAdmin):
    list_display = ( 'postulacion', 'cliente', 'cargo','examenes')
    search_fields = ( 'postulacion', 'cliente')
    list_filter = ('cliente', 'cargo')

    def has_add_permission(self, request, obj=None):
        return True