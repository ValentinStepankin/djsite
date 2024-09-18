# файл нужен для хранения представлений/контроллеров приложения
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *


menu = [{'title': "O caйтe", 'url_name': 'about'},
        {'title': "Дoбавить статью", 'url_name': 'add_page'},
        {'title': "0братная связь", 'url_name': 'contact'},
        {'title': "Boйти", 'url_name': 'login'},
]
def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")



def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')
