from django.core.management.base import BaseCommand,CommandError
from ...apps.accounts.models import Rating,PointCount,Discount
from ...eshop.devs import DISCOUNT_TRESHOLDS


class MonthlyUpdatePointCount(BaseCommand): #update discount 14th of every month
    help = "At the beginning of every month, the new points collecting season starts."
    def handle(self,*args,**options):
        for el in Discount.objects.all():
            pointcount = Discount.pointcount
            points = pointcount.points
            el.prev_count = points
            el.save()
            pointcount.points = 0
            pointcount.save()


