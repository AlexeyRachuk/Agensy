from django.db import models
from django.urls import reverse
from datetime import date

from estate_agents.models import Agent


class PropertyType(models.Model):
    name = models.CharField('Название', max_length=100)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип объекта"
        verbose_name_plural = "Типы объекта"


class PropertyGallery(models.Model):
    name = models.CharField('Название галереи', max_length=100)
    image1 = models.ImageField('Фото объекта 1', upload_to="property_photos/", help_text='Певрое фото обязательное, осатльные нет')
    image2 = models.ImageField('Фото объекта 2', upload_to="property_photos/", blank=True)
    image3 = models.ImageField('Фото объекта 3', upload_to="property_photos/", blank=True)
    image4 = models.ImageField('Фото объекта 4', upload_to="property_photos/", blank=True)
    image5 = models.ImageField('Фото объекта 5', upload_to="property_photos/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Галерея объекта"
        verbose_name_plural = "Галереи объекта"


class PropertyOptions(models.Model):
    name = models.CharField('Название опции', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Опция"
        verbose_name_plural = "Опции"


class Property(models.Model):
    name = models.CharField('Название объекта', max_length=100)
    price = models.PositiveIntegerField('Цена объекта', help_text='Цена в ₽')
    descripton = models.TextField('Описание объекта')
    property_id = models.PositiveSmallIntegerField('ID объекта')
    location = models.CharField('Расположение', max_length=150)
    type = models.ForeignKey(PropertyType, verbose_name='Тип объекта', on_delete=models.SET_NULL,
                             null=True)
    area = models.PositiveSmallIntegerField('Площадь', blank=True)
    room = models.PositiveSmallIntegerField('Кол-во комнат', blank=True)
    baths = models.PositiveSmallIntegerField('Кол-во ванных комнат', blank=True)
    garage = models.PositiveSmallIntegerField('Кол-во гаражей', blank=True, null=True)
    photo_preview = models.ImageField('Фото для списка', upload_to="property_preview/", null=True)
    photo_main = models.ForeignKey(PropertyGallery, verbose_name='Галерея объекта', on_delete=models.SET_NULL,
                                   null=True)
    options = models.ManyToManyField(PropertyOptions, verbose_name='Опиции', related_name='options_list')
    video = models.URLField('Ссылка на видео объекта', max_length=150, blank=True)
    plans = models.ImageField('План проекта', upload_to="property_plans/", blank=True)
    map = models.CharField('Ссылка на карту', max_length=500, help_text='frame карты', blank=True)
    agent = models.ForeignKey(Agent, verbose_name='Агент', on_delete=models.SET_NULL,
                              null=True, related_name='agent_property')
    url = models.SlugField(max_length=130, unique=True)
    date = models.DateField('Дата публикации', default=date.today)
    is_slider = models.BooleanField('Отобажать в слайдере', default=False)
    draft = models.BooleanField("Публикация", default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("property_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"
