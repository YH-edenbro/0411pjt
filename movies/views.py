from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import CreateForm, CommentForm

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
    else:
        form = CreateForm()
    context = {
        'form':form
    }
    return render(request, 'movies/create.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    commeent_form = CommentForm()
    context = {
        'movie':movie,
        'comment_form': commeent_form,
    }
    return render(request, 'movies/detail.html', context)

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

def comments_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie_id = movie
        comment.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'movie':movie,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.html', context)

def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)