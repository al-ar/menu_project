from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Menu, MenuItem


class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        obj.slug = obj.menu_name.name + '/' + obj.slug
        obj.save()

class MenuMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(Menu, MenuMPTTModelAdmin)
admin.site.register(MenuItem, MenuItemMPTTModelAdmin)
