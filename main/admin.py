from django.contrib import admin
from .models import *


class AvtobusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class DoorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Avtobus, AvtobusAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Door, DoorAdmin)


