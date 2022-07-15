from django.core.management.base import BaseCommand,CommandError
from ...models import Rating,PointCount,Discount


class Command(BaseCommand): #update discount 14th of every month
    help = "At the beginning of every month, the new points collecting season starts."
    def handle(self,*args,**options):
        for el in Discount.objects.all():
            pointcount = el.pointcount
            points = pointcount.points
            el.prev_count = points
            el.save()
            pointcount.points = 0
            pointcount.save()
        self.stdout.write("Season updated!")


