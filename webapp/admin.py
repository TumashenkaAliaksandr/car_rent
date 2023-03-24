from django.contrib import admin
from django.utils.safestring import mark_safe

from webapp.models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields = ('title', 'door_num', 'seat_num', 'transmission', 'rating', 'price', 'photo', 'is_main',)
    readonly_fields = ('preview_photo',)
    list_display = ('pk', 'title', 'door_num', 'seat_num', 'transmission', 'is_main',)
    list_display_links = ('title',)
    list_editable = ('is_main',)
    list_filter = ('door_num', 'seat_num', 'rating', 'is_main', 'transmission',)
    search_fields = ('title',)

    def preview_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="150" />')
    preview_photo.short_description = 'Preview_photo'