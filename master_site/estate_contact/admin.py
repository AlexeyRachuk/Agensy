from django import forms
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Contact, FormContactPage

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AboutAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание страницы', widget=CKEditorUploadingWidget())

    class Meta:
        model = Contact
        fields = '__all__'


@admin.register(Contact)
class AboutAdminForm(SingletonModelAdmin):
    fields = ('name', 'text', 'map', 'email', 'phone', 'address', 'facebook', 'twitter', 'instagram',)
    form = AboutAdminForm


@admin.register(FormContactPage)
class FormContactPageAdmin(admin.ModelAdmin):
    list_display = ('name',)
