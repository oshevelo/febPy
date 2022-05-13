from django.contrib import admin

# Register your models here.
from .models import Rating, PointCount, Discount

class RatingAdmin(admin.ModelAdmin):
    fields=['percentile','user_points','user_id']
admin.site.register(Rating,RatingAdmin)

class PointCountAdmin(admin.ModelAdmin):
    fields=['user_id','points',]

admin.site.register(PointCount,PointCountAdmin)

class DiscountAdmin(admin.ModelAdmin):
    fields=['user_id','user_point','percent_to_pay','discount']
admin.site.register(Discount)
