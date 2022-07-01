from django.contrib import admin

# Register your models here.

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_type', 'user', 'date_created')
    list_filter = ['order_type']
    date_hierarchy = 'date_created'
    search_fields = ['user']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    raw_id_fields = ['order']

admin.site.register(OrderItem)
