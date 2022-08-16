from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from ckeditor.widgets import CKEditorWidget



class UsuarioForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField()
    edad=forms.IntegerField()
    pais=forms.CharField(max_length=50)
  
class ColaboradorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField()
    edad=forms.IntegerField()
    especialidad=forms.CharField(max_length=50)
   
class StaffForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField()
    edad=forms.IntegerField()
    categoria=forms.CharField(max_length=50)

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email= forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name'] 
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):    
    imagen= forms.ImageField(label="Imagen")


class PosteoForm(forms.Form):
    titulo= forms.CharField(max_length=100)
    descripcion= forms.CharField()
    contenido= forms.CharField()

class PosteoUltimasNoticiasForm(forms.Form):
    titulo= forms.CharField(max_length=100)
    descripcion= forms.CharField()
    contenido= forms.CharField(widget=CKEditorWidget())
    foto= forms.FileField(widget=forms.ClearableFileInput(), required=False)

class PosteoEconomiaForm(forms.Form):
    titulo= forms.CharField(max_length=100)
    descripcion= forms.CharField()
    contenido= forms.CharField(widget=CKEditorWidget())
    foto= forms.FileField(widget=forms.ClearableFileInput(), required=False)

class PosteoDeportesForm(forms.Form):
    titulo= forms.CharField(max_length=100)
    descripcion= forms.CharField()
    contenido= forms.CharField(widget=CKEditorWidget())
    foto= forms.FileField(widget=forms.ClearableFileInput(), required=False)
   
class PosteoEspectaculosForm(forms.Form):
    titulo= forms.CharField(max_length=100)
    descripcion= forms.CharField()
    contenido= forms.CharField(widget=CKEditorWidget())
    foto= forms.FileField(widget=forms.ClearableFileInput(), required=False)
    
    


    