from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Название категории', max_length=60)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.url})

    class Meta:
        verbose_name = "Категория блога"
        verbose_name_plural = "Категории блога"


class Blog(models.Model):
    seo_title = models.CharField('SEO заголовок', max_length=70)
    seo_descr = models.CharField('SEO описание', max_length=150)
    name = models.CharField('Название статьи', max_length=150)
    category = models.ForeignKey(Category, verbose_name='Категория статьи', on_delete=models.SET_NULL, null=True)
    autor = models.CharField('Автор статьи', max_length=60)
    date = models.DateField('Дата публикации', default=date.today)
    image_preview = models.ImageField('Превью изображения', upload_to="blog_preview/")
    image_main = models.ImageField('Основное изображение', upload_to="blog_main/")
    text_preview = models.TextField('Вводный текст')
    text_main = models.TextField('Текст статьи')
    text_quote = models.TextField('Цитата', blank=True)
    quote_autor = models.CharField('Автор цитаты', max_length=60, blank=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Публикация", default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"
