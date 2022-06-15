from django.shortcuts import render

from estate_about.models import About


def about_page(request):
    return render(request, 'about/about.html', {'abouts': About.objects.all(), 'title': 'О компании'})
