from django import forms
from django.contrib import admin

from .models import Blog, Category

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogAdminForm(forms.ModelForm):
    text_preview = forms.CharField(label='Текст превью',  widget=CKEditorUploadingWidget())
    text_main = forms.CharField(label='Основной текст', widget=CKEditorUploadingWidget())
    text_quote = forms.CharField(label='Текст цитаты', required=False, widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


@admin.register(Blog)
class BlogAdminForm(admin.ModelAdmin):
    list_display = ('name', 'category', 'date', 'draft')
    list_filter = ('category',)
    search_fields = ('name', 'date')
    list_editable = ('draft',)
    prepopulated_fields = {'url': ('name',)}
    form = BlogAdminForm


@admin.register(Category)
class CategoryAdminForm(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'url': ('name',)}