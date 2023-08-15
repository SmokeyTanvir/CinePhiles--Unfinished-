from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def home(request):
    context = {
        'movies': models.Movie.objects.all(),
    }

    return render(request, 'home.html', context)

def movie(request, id):
    movie = models.Movie.objects.get(id=id)
    casts = movie.cast.all()

    context = {
        'movie': movie,
        'casts': casts 
    }

    return render(request, 'movie.html', context)