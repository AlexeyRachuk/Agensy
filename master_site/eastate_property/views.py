from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Property, PropertyType
from .serializers import PropertySerializer


class TypeFilter:
    def get_types(self):
        return PropertyType.objects.all()


class PropertyView(TypeFilter, ListView):
    model = Property
    queryset = Property.objects.filter(draft=True).order_by('-date')
    template_name = 'property/property-grid.html'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Объекты'
        return context


class FilterPropertyView(TypeFilter, ListView):
    template_name = 'property/property-grid.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = Property.objects.filter(type__in=self.request.GET.getlist('type'))
        return queryset


class PropertyDetailView(TypeFilter, DetailView):
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
