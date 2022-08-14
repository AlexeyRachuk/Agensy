from django import forms
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Sites, Index, Benefits, Review

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from metatags.admin import MetaTagInline


class CustomModelAdmin(admin.ModelAdmin):
    inlines = (MetaTagInline,)


class BenefitsInline(admin.TabularInline):
    model = Benefits
    extra = 1


# class ReviewAdminForm(forms.ModelForm):
#    descr = forms.CharField(label='Отзыв', widget=CKEditorUploadingWidget())
#
#   class Meta:
#       model = Review
#       fields = '__all__'

# @admin.register(Review)
# class ReviewAdminForm(admin.ModelAdmin):
#    list_display = (
#        'name', 'descr', 'photo',)
#    form = ReviewAdminForm


class ReviewInline(admin.TabularInline, forms.ModelForm):
    model = Review
    extra = 1


@admin.register(Sites)
class SitesAdminForm(admin.ModelAdmin):
    list_display = (
        'title', 'url',)


class IndexAdminForm(forms.ModelForm):
    descr = forms.CharField(label='Текст в подвале', widget=CKEditorUploadingWidget())

    class Meta:
        model = Index
        fields = '__all__'


@admin.register(Index)
class IndexAdminForm(SingletonModelAdmin):
    filter_horizontal = ('sites',)
    inlines = [BenefitsInline, ReviewInline, ]
    form = IndexAdminForm

#
#
# class BenefitsAdminForm(forms.ModelForm):
#   descr = forms.CharField(label='Текст преимущества', widget=CKEditorUploadingWidget())
#
#    class Meta:
#        model = Benefits
#        fields = '__all__'


# @admin.register(Benefits)
# class BenefitsAdminForm(admin.ModelAdmin):
#    list_display = (
#        'name', 'descr',)
#    form = BenefitsAdminForm


# @admin.register(Slider)
# class SliderAdminForm(admin.ModelAdmin):
#    filter_horizontal = ('slider',)
