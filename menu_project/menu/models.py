from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=200, verbose_name='титл')
    slug = models.SlugField(unique=True, verbose_name='адрес')
    description = models.TextField(verbose_name='описание')


    def __str__(self):
        return self.title
