from django.contrib import admin

from .models import Menu


# class MenuAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'titles',)
#     empty_value_display = '-пусто-'

admin.site.register(Menu)