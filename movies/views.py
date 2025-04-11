from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import CreateForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    context = {
        'form':form
    }
    return render(request, 'movies/create.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie':movie
    }
    return render(request, 'movies', context)

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    form = CreateForm(request.POST, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')