from django.urls import path
from . import views

app_name = 'contratacion' 
urlpatterns = [
    path('crear_candidato/', views.CrearCandidato.as_view(), name='crear_candidato'),
    path('editar_candidato/<int:pk>/', views.EditarCandidato.as_view(), name='editar_candidato'),
    path('eliminar_candidato/<int:pk>/', views.EliminarCandidato.as_view(), name='eliminar_candidato'),
    path('crear_oferta/', views.CrearOferta.as_view(), name='crear_oferta'),
    path('editar_oferta/<int:pk>/', views.EditarOferta.as_view(), name='editar_oferta'),
    path('eliminar_oferta/<int:pk>/', views.EliminarOferta.as_view(), name='eliminar_oferta'),
    path('crear_postulacion/', views.CrearPostulacion.as_view(), name='crear_postulacion'),
    path('editar_postulacion/<int:pk>/', views.EditarPostulacion.as_view(), name='editar_postulacion'),
    path('eliminar_postulacion/<int:pk>/', views.EliminarPostulacion.as_view(), name='eliminar_postulacion'),
    path('crear_orden/', views.CrearOrdenDeContratacion.as_view(), name='crear_orden'),
    path('editar_orden/<int:pk>/', views.EditarOrdenDeContratacion.as_view(), name='editar_orden'),
    path('eliminar_orden/<int:pk>/', views.EliminarOrdenDeContratacion.as_view(), name='eliminar_orden'),
]