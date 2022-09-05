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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['type'] = f'type={self.request.GET.get("type")}&'
        return context


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


class Search(ListView):
    paginate_by = 9
    template_name = 'property/property-grid.html'

    def get_queryset(self):
        q = self.request.GET.get('q').capitalize()
        return Property.objects.filter(name__icontains=q)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f'q={self.request.GET.get("q")}&'
        return context


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
