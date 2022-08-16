from distutils.command.upload import upload
from pickle import TRUE
from ssl import Options
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField


class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    edad=models.IntegerField()
    pais=models.CharField(max_length=50)

    def __str__(self):
        return "nombre:"+" "+self.nombre+" "+"E-mail:"+" "+self.email+" "+"Edad:"+" "+str(self.edad)+" "+"País:"+" "+self.pais

class Colaborador(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    edad=models.IntegerField()
    especialidad=models.CharField(max_length=50)

    def __str__(self):
        return "nombre:"+" "+self.nombre+" "+"E-mail:"+" "+self.email+" "+"Edad:"+" "+str(self.edad)+" "+"Especialidad:"+" "+self.especialidad

class Staff(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    edad=models.IntegerField()
    categoria=models.CharField(max_length=50)
    
    def __str__(self):
        return "nombre:"+" "+self.nombre+" "+"E-mail:"+" "+self.email+" "+"Edad:"+" "+str(self.edad)+" "+"Categoria:"+" "+self.categoria


class Avatar(models.Model):    
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)   

class Posteo(models.Model):     
    titulo= models.CharField(max_length=100)
    descripcion= models.TextField(null=True)
    contenido= models.TextField()    
    publicado= models.DateTimeField(default=timezone.now)
    autor= models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post", null=TRUE)    

    def __str__(self):
        return self.titulo

class Comentarios(models.Model):
    posteo= models.ForeignKey(Posteo, on_delete=models.CASCADE, related_name="comentarios")
    nombre= models.CharField(max_length=50)
    email= models.EmailField()
    contenido= models.TextField()
    publicado= models.DateTimeField(auto_now_add=True)
    estado= models.BooleanField(default=True)

    def __str__(self):
        return f"Comentario de {self.nombre}"


class PosteoUltimasNoticias(models.Model):    
    titulo= models.CharField(max_length=150)
    descripcion= RichTextField(null=True)
    foto= models.ImageField(upload_to='imagenes', null=True, blank=True)
    contenido= RichTextField()
    publicado= models.DateTimeField(default=timezone.now)
    autor= models.ForeignKey(User, on_delete=models.CASCADE,null=TRUE)
    
    def __str__(self):
        return self.titulo

class PosteoEconomia(models.Model):
    titulo= models.CharField(max_length=100)
    descripcion= models.TextField(null=True)
    foto= models.ImageField(upload_to='imagenes', null=True, blank=True)
    contenido= RichTextField()
    publicado= models.DateTimeField(default=timezone.now)
    autor= models.ForeignKey(User, on_delete=models.CASCADE,null=TRUE)
    
    def __str__(self):
        return self.titulo

class PosteoDeportes(models.Model):    
    titulo= models.CharField(max_length=150)
    descripcion= RichTextField(null=True)
    foto= models.ImageField(upload_to='imagenes', null=True, blank=True)
    contenido= RichTextField()
    publicado= models.DateTimeField(default=timezone.now)
    autor= models.ForeignKey(User, on_delete=models.CASCADE,null=TRUE)
    
    def __str__(self):
        return self.titulo

class PosteoEspectaculos(models.Model):
    titulo= models.CharField(max_length=100)
    descripcion= models.TextField(null=True)  
    foto= models.ImageField(upload_to='imagenes', null=True, blank=True)  
    contenido= RichTextField()
    publicado= models.DateTimeField(default=timezone.now)
    autor= models.ForeignKey(User, on_delete=models.CASCADE,null=TRUE)
    
    def __str__(self):
        return self.titulo

class Imagen(models.Model):    
    imagen= models.ImageField(upload_to='imagenes', null=True, blank=True)  


   
