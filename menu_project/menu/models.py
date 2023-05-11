from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    name = models.CharField(max_length=100,
                            verbose_name='Название меню')
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(MPTTModel):
    title = models.CharField(max_length=200, verbose_name='название')
    slug = models.SlugField(unique=True, verbose_name='адрес')
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children')
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE,
                                  verbose_name='Название меню')


    class MPTTMeta:
        order_insertion_by = ['position']
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


    def __str__(self):
        return self.title
