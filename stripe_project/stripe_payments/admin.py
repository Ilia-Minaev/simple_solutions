from django.contrib import admin
from .models import Items


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_display_links = ('name',)
    fields = ('name', 'description', 'price',)
    #prepopulated_fields = {'slug': ('title',)}


admin.site.register(Items, ItemAdmin)
