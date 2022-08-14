from django import forms
from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Property, PropertyGallery, PropertyOptions, PropertyType


class PropertyAdminForm(forms.ModelForm):
    descripton = forms.CharField(label='Текст превью', widget=CKEditorUploadingWidget())

    class Meta:
        model = Property
        fields = '__all__'


admin.site.register(PropertyGallery)
admin.site.register(PropertyOptions)
admin.site.register(PropertyType)


@admin.register(Property)
class PropertyAdminForm(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'agent', 'date',  'draft')
    list_filter = ('type', 'agent', 'date')
    search_fields = ('name', 'price')
    list_editable = ('draft',)
    prepopulated_fields = {'url': ('name',)}
    filter_horizontal = ('options',)
    form = PropertyAdminForm
