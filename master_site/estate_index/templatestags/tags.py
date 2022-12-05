from django import template
from estate_blog.models import Blog
from estate_agents.models import Agent
from eastate_property.models import Property, PropertyType

register = template.Library()


@register.inclusion_tag('tags/last_blogs.html')
def get_last_articles():
    last_blog = Blog.objects.order_by('-date')[0:6]
    return {'last_blogs': last_blog}


@register.inclusion_tag('tags/best_agents.html')
def get_bets_agents():
    best_agent = Agent.objects.filter(best=True)
    return {'best_agents': best_agent}


@register.inclusion_tag('tags/last_property.html')
def get_last_property():
    last_property = Property.objects.order_by('-date')[0:6]
    return {'last_propetys': last_property}


@register.inclusion_tag('tags/slider.html')
def get_property_slider():
    slider = Property.objects.filter(is_slider=True).order_by('-date')
    return {'sliders': slider}
