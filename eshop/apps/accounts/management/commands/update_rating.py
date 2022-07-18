from django.core.management.base import BaseCommand,CommandError
from ...models import Rating,PointCount,Discount


def get_points(rating):
    pointcount = rating.pointcount
    return pointcount.points

class Command(BaseCommand): #update discount 14th of every month
    help = "At the beginning of every month, the new points collecting season starts."
    def handle(self,*args,**options):
        ratings = list(Rating.objects.all())
        ratings.sort(key=get_points)
        total_ratings = len(ratings)
        for i,el in enumerate(ratings):
            new_rate = (i+1)/total_ratings * 100
            el.percentile = new_rate
            el.save()
        self.stdout.write("Rating updated!")
