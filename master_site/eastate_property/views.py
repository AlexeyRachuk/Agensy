from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Property
from .serializers import PropertySerializer


class PropertyView(ListView):
    model = Property
    queryset = Property.objects.filter(draft=True)
    template_name = 'property/property-grid.html'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Объекты'
        return context


class PropertyCategory(ListView):
    slug_field = 'url'
    template_name = 'property/property-grid.html'
    context_object_name = 'property_list'


class PropertyDetailView(DetailView):
    model = Property
    slug_field = 'url'
    template_name = 'property/property-single.html'
    context_object_name = 'property'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Объект | ' + str(context['property'].name)
        return context


class PropertyOptions(ListView):
    model = Property
    context_object_name = 'options_list'


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
