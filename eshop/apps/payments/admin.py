from django.contrib import admin

from .models import Payment, PaymentSystemLog


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('system', 'status', 'products_price', 'delivery_price')
    list_filter = ['status']
    search_fields = ['system']


admin.site.register(Payment, PaymentAdmin)


class PaymentSystemLogAdmin(admin.ModelAdmin):
    list_display = ('payment', 'request_data', 'response_data', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


admin.site.register(PaymentSystemLog, PaymentSystemLogAdmin)



