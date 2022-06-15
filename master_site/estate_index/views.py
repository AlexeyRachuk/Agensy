from django.shortcuts import render

from estate_index.models import Index



def index(request):
    return render(request, 'index/index.html', {'indexs': Index.objects.all(), 'title': 'Главная'})


def last_article():
    last_pages = estate_blog.Blog.objects.order_by("-date")[0:6]
    return {
        'last_pages': last_pages,
    }
