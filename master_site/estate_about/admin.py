from django import forms
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import About

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AboutAdminForm(forms.ModelForm):
    page_descr = forms.CharField(label='Текст превью', widget=CKEditorUploadingWidget())

    class Meta:
        model = About
        fields = '__all__'


@admin.register(About)
class AboutAdminForm(SingletonModelAdmin):
    fields = (
        'title', 'banner_photo', 'banner_title', 'banner_descr', 'page_photo', 'page_title', 'page_descr',
        'agent_about')
    filter_horizontal = ('agent_about',)
    form = AboutAdminForm
