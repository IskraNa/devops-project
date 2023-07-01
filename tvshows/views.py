from django.shortcuts import render, redirect
from .models import TVShow


def index(request):
    return render(request, 'base.html')


def shows(request):
    tvshows = TVShow.objects.all()
    context = {"tvshows": tvshows}
    return render(request, 'shows.html', context)


def tvshow_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        genre = request.POST['genre']
        release_date = request.POST['release_date']
        TVShow.objects.create(title=title, description=description, genre=genre, release_date=release_date)
        return redirect('/')
    return render(request, 'tvshow_create.html')


def tvshow_update(request, pk):
    tvshow = TVShow.objects.get(pk=pk)
    if request.method == 'POST':
        tvshow.title = request.POST['title']
        tvshow.description = request.POST['description']
        tvshow.genre = request.POST['genre']
        tvshow.release_date = request.POST['release_date']
        tvshow.save()
        return redirect('index')
    return render(request, 'tvshow_update.html', {'tvshow': tvshow})


def tvshow_delete(request, pk):
    tvshow = TVShow.objects.get(pk=pk)
    tvshow.delete()
    return redirect('/')
