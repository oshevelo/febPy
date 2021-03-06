from django.core.management.base import BaseCommand,CommandError
from ...models import Discount,PointCount

DISCOUNT_TRESHOLDS = {100:0.05,
                      500:0.075,
                      1200:0.1,
                      5000:0.2}



class Command(BaseCommand): #update discount 14th of every month
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
        self.stdout.write("Discounts updated!")
