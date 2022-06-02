from django.contrib import admin

# Register your models here.
from .models import Rating, PointCount, Discount

class RatingAdmin(admin.ModelAdmin):
    fields=['percentile','points','user']


class PointCountAdmin(admin.ModelAdmin):
    fields=['user_id','points']

class DiscountAdmin(admin.ModelAdmin):
    fields=['user','pointcount','discount','prev_count']


admin.site.register(Discount,DiscountAdmin)
admin.site.register(PointCount,PointCountAdmin)
admin.site.register(Rating,RatingAdmin)