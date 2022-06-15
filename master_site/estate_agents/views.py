from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Agent

class AgentView(ListView):
    model = Agent
    queryset = Agent.objects.filter(draft=True)
    template_name = 'agent/agents-grid.html'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Агенты'
        return context


class AgentDetailView(DetailView):
    model = Agent
    slug_field = 'url'
    template_name = 'agent/agent-single.html'
    context_object_name = 'agent'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Агент | ' + str(context['agent'].name)
        return context