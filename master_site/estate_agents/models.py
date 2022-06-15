from django.db import models
from django.urls import reverse


class Agent(models.Model):
    name = models.CharField('Имя Агента', max_length=150)
    description = models.TextField('Описание агента', max_length=300, help_text='Описание на 300 символов')
    property_agent = models.ManyToManyField(to='eastate_property.Property', verbose_name='Обеъекты агента',
                                            related_name='property_agent')
    photo = models.ImageField('Фото агента', upload_to="agents/")
    phone = models.CharField('Номер телефона', max_length=10, help_text='Номер без +7')
    email = models.EmailField('Email')
    facebook = models.CharField('Facebook', max_length=60, blank=True)
    twitter = models.CharField('Twitter', max_length=60, blank=True)
    instagram = models.CharField('Instagram', max_length=60, blank=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Публикация", default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("agent_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Агент"
        verbose_name_plural = "Агенты"
