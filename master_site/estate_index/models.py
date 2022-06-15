from django.db import models
from django.db.models import Index
from django.urls import reverse
from solo.models import SingletonModel


class Sites(models.Model):
    title = models.CharField('Название сайта', max_length=100)
    url = models.CharField('Ccылка на сайт', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сайты в подвале"
        verbose_name_plural = "Сайты в подвале"


class Meta:
    verbose_name = "Преимущества"
    verbose_name_plural = "Преимущества"


class Index(SingletonModel):
    singleton_instance_id = 1
    title = models.CharField('Название компании', max_length=50)
    slider = models.ManyToManyField(to='eastate_property.Property', verbose_name='Обеъекты слайдера',
                                    related_name='property_index')
    index_agents = models.ManyToManyField(to='estate_agents.Agent', verbose_name='Лушие агенты',
                                          related_name='index_agents')
    index_property = models.ManyToManyField(to='eastate_property.Property', verbose_name='Новые объекты',
                                            related_name='index_property')
    descr = models.TextField('Описание в подвале', max_length=500)
    phone = models.CharField('Номер телефона в подвале', max_length=10, help_text='Номер без +7')
    email = models.EmailField('Email в подвале')
    sites = models.ManyToManyField(Sites, verbose_name='Сайты в подвале', related_name='sites_list')
    copywrite = models.CharField('Копирайт в подвале', max_length=100)
    facebook = models.CharField('Facebook в подвале', max_length=60, blank=True)
    twitter = models.CharField('Twitter в подвале', max_length=60, blank=True)
    instagram = models.CharField('Instagram в подвале', max_length=60, blank=True)

    def __str__(self):
        return "Главная"

    class Meta:
        verbose_name = "Главная"


class Benefits(models.Model):
    name = models.CharField('Название преимущества', max_length=100)
    descr = models.CharField('Описание преимущества', max_length=500)
    benefits = models.ForeignKey(Index, on_delete=models.CASCADE, related_name='benefits_id', default='')


class Review(models.Model):
    name = models.CharField('Имя отзыва', max_length=100)
    descr = models.TextField('Отзыв', max_length=500)
    photo = models.ImageField('Фото отзыва', upload_to="review/", null=True)
    review = models.ForeignKey(Index, on_delete=models.CASCADE, related_name='review_id', default='')

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"
