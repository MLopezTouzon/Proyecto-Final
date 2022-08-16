from django import forms
from .models import *
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget




class MensajeForm(forms.Form):
    destinatario= forms.CharField(max_length=25)
    asunto= forms.CharField(max_length=75)
    cuerpo= forms.CharField(widget=CKEditorWidget())
    
    