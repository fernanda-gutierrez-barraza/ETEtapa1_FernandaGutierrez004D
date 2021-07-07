from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Pais, Periodista




class ObjetoForm(forms.ModelForm):
    
    nombreCompleto = forms.CharField(label='Nombre',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'name': 'Nombre',
            'placeholder': 'Ingrese el nombre completo'
        }
    ))
    
    rut = forms.CharField(label='Rut', max_length=10, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'name': 'Rut',
            'placeholder': 'Ingrese rut del periodista'
        }
    ))

    telefono = forms.IntegerField(label='Telefóno', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'name': 'Telefono',
            'placeholder': 'Ingrese telefóno del periodista'
        }
    ))

    email = forms.CharField(label='Email', max_length=50, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'name': 'Email',
            'placeholder': 'Ingrese email del periodista'
        }
    ))

    direccion = forms.CharField(label='Dirección', max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'name': 'Direccion',
            'placeholder': 'Ingrese dirección del periodista'
        }
    ))
    
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), label='País',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
            ))

    contraseña = forms.CharField(label='Contraseña', max_length=50, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'name': 'Contraseña',
            'placeholder': 'Contraseña del periodista'
        }
    ))

    image = forms.ImageField(label='Imagen',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))
    

    class Meta:
        model = Periodista
        fields = ('nombreCompleto','rut', 'telefono', 'email','direccion','pais','contraseña','image')