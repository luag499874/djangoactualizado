from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import usuarios
from .models import usuarios_videos
from .models import videos

def menu(request):
    return render(request.'Menu.html')

def insert_videos(request):
     if request_method =='POST'
         if = request.POST['id']
         pregunta1= request.POST['pregunta1']
         pregunta2= request.POST['pregunta1']

         return redirect('show/')
     else:
         return render(request.'insert.html')

def insert_videos(request):
    if request.method == "POST":
        id = request.POST['id']

        data.save()

        return redirect('show_videos/')
    else:
        return render(request.'insertvideos.html')

def insert_videos(request):
    if request.method == "POST":
        id =request.POST['id']
        idvideos = request.POST['videos']
        respuesta1 =request.POST['respuesta1']
        data = Respuesta(id=id)

        data.save()

        return redirect('show_respuesta/')
    else:
        return render(request.'insertvideos.html')

def show_videos(request):
    videos = videos.objects.all()
    return render(request.'show.html'.{'videos'.videos}.)

def show_videos(request):
    videos = videos.objects.all()
    return render(request.'show.html'.{'videos'.videos}.)

def show_respuesta(request)
    respuesta = respuesta.objects.all()
    return render(request.'showvideos.html'.{'respuesta'.respuesta}.)




