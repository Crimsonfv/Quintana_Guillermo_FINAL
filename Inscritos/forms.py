from django import forms
from .models import Inscritos, Instituciones

estados = [
    ('RESERVADO', 'RESERVADO'),
    ('COMPLETADA', 'COMPLETADA'),
    ('ANULADA', 'ANULADA'),
    ('NO ASISTEN', 'NO ASISTEN'),
]

class InscritosForm(forms.ModelForm):
    Nombre = forms.CharField(label='Nombre', max_length=80, required=True, widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'Ingrese solo letras',"class":"form-control"})) 
    Telefono = forms.CharField(label='Telefono', max_length=50, required=True, widget=forms.TextInput(attrs={'pattern': '[0-9+]+', 'title': 'Ingrese solo números',"class":"form-control"}),)
    FechaDeInscripcionYHora = forms.DateTimeField(label='Fecha y Hora de Reserva', required=True, input_formats=['%Y-%m-%d %H:%M'],widget=forms.DateTimeInput(attrs={'placeholder': '2022-12-22 18:00', "class":"form-control", "type":"datetime"}),error_messages={'invalid': 'Por favor, introduce una fecha y hora válidas. Por ejemplo: 2022-12-14 18:00.',})
    Estado = forms.ChoiceField(label='Estado', required=True, choices=estados, widget=forms.Select(attrs={"class":"form-control"}))
    Institucion = forms.ModelChoiceField(label='Institución', required=True, queryset=Instituciones.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))
    Observaciones = forms.CharField(label='Observaciones', required=False,widget=forms.Textarea(attrs={"class":"form-control", "rows":"4"}))

    class Meta:
        model = Inscritos
        fields = ('Nombre', 'Telefono', 'FechaDeInscripcionYHora', 'Estado', 'Institucion', 'Observaciones')

class InstitucionesForm(forms.ModelForm):
    Nombre = forms.CharField(label='Nombre', max_length=80, required=True, widget=forms.TextInput(attrs={"class":"form-control"})) 

    class Meta:
        model = Instituciones
        fields = ('Nombre',)