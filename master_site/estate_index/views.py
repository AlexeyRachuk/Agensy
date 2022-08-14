from django.shortcuts import render

from estate_index.models import Index

from estate_blog.models import Blog


def index(request):
    return render(request, 'index/index.html', {'indexs': Index.objects.all(), 'title': 'Главная'})
