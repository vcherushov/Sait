from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *
from .forms import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},

]

class AvtobusHome(ListView):
    model = Avtobus
    template_name = 'main/index.html'
    context_object_name = 'post'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        return context

#def index(request):
    #post = Avtobus.objects.all()
    #context = {
        #'post': post,
        #'menu': menu,
        #'title': 'Главная страница',
        #'cat_selected': 0,
    #}
    #return render(request, 'main/index.html', context=context)



def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    form = AddPostForm(request.POST, request.FILES)
    if form.is_valid():
        try:
            form.save()
            return redirect('home')
        except:
            form.add_error(None, 'Ошибка добавления')
    else:
        form = AddPostForm()
    return render(request, 'main/addpage.html', {'form': form,'menu': menu, 'title': 'Добавление видео'})



def contact(request):
    return HttpResponse("Обратная связь")






def show_post(request, post_slug):
    post = Avtobus.objects.filter(slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': 'Видео',
        'cat_selected': 0,
    }
    return render(request, 'main/post.html', context=context)



def show_category(request):
    post = Avtobus.objects.all()
    form = AddPostForm(request.GET)
    if form.is_valid():

        if form.cleaned_data["door"]:
            post = post.filter(door=form.cleaned_data["door"])

        if form.cleaned_data["time_create"]:
            post = post.filter(time_create=form.cleaned_data["time_create"])

        if form.cleaned_data["time_time"]:
            post = post.filter(time_time=form.cleaned_data["time_time"])

    context = {
        'post': post,
        'menu': menu,
        'form': form,
        'title': 'Видео с автобусов',
        'cat_selected': 0,
    }

    return render(request, 'main/category.html', context=context)






def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Не найдена</h1>')
