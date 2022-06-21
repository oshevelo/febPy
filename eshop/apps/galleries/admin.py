from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'upload')
    list_filter = ['size']
    search_fields = ['product']


admin.site.register(Image, ImageAdmin)






