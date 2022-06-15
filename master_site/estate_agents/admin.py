from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Agent


@admin.register(Agent)
class AgentAdminForm(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'draft')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'url': ('name',)}
    filter_horizontal = ('property_agent',)
    list_editable = ('draft',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60"')

    get_image.short_description = 'Фото'