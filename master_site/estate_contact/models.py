from django.db import models
from solo.models import SingletonModel


class FormContactPage(models.Model):
    name = models.CharField('Имя', max_length=20)
    email = models.CharField('Enail', max_length=50)
    subject = models.CharField('Тема обращения', max_length=100, blank='True')
    message = models.CharField('Сообщение', max_length=255)

    class Meta:
        verbose_name = "Заявки с формы на странице Контакты"
        verbose_name_plural = "Заявки с формы на странице Контакты"

    def __str__(self):
        return "Заявки с формы на странице Контакты"


class Contact(SingletonModel):
    singleton_instance_id = 1
    name = models.CharField('Название страницы', max_length=100)
    text = models.CharField('Описание страницы', max_length=500)
    map = models.CharField('Ссылка на карту', max_length=500, help_text='frame карты', blank=True)
    phone = models.CharField('Номер телефона', max_length=10, help_text='Номер без +7')
    email = models.EmailField('Email')
    address = models.TextField('Адрес', max_length=200)
    facebook = models.CharField('Facebook', max_length=60, blank=True)
    twitter = models.CharField('Twitter', max_length=60, blank=True)
    instagram = models.CharField('Instagram', max_length=60, blank=True)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return "Контакты"
