from django.core.management.base import BaseCommand,CommandError
from ...apps.accounts.models import Rating,PointCount,Discount
from ...eshop.devs import DISCOUNT_TRESHOLDS

class MonthlyUpdateDiscount(BaseCommand): #update discount 14th of every month
    help = "At the 14th of every month, the Discount is updated based on the previous month points count."
    def handle(self,*args,**options):
        for el in Discount.objects.all():
            points = el.prev_count
            discount = 0
            for key,val in DISCOUNT_TRESHOLDS.items():
                if points>key:
                    discount = val
            el.discount = discount
            el.save()
