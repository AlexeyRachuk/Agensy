from django.db import models
from estate_agents.models import Agent
from solo.models import SingletonModel


class About(SingletonModel):
    singleton_instance_id = 1
    title = models.CharField('Название страницы', max_length=200)
    banner_photo = models.ImageField('Баннер страницы', upload_to="about/")
    banner_title = models.CharField('Заголовок баннера', max_length=200)
    banner_descr = models.CharField('Описание баннера', max_length=100)
    page_photo = models.ImageField('Фото страницы', upload_to="about/")
    page_title = models.CharField('Заголовок страницы', max_length=100)
    page_descr = models.TextField('Текст страницы')
    agent_about = models.ManyToManyField(Agent, verbose_name='Агенты', related_name='agent_about')

    def __str__(self):
        return "О компании"

    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "О компании"
