from django import forms
from . import models as m

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = m.Candidato
        fields = '__all__'

class OfertaForm(forms.ModelForm):
    class Meta:
        model = m.OfertaLaboral
        fields = '__all__'

class PostulacionForm(forms.ModelForm):
    class Meta:
        model = m.Postulacion
        fields = '__all__'
