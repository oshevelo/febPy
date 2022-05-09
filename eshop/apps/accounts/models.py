from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class PointCount(models.Model):
    _user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    _points = models.FloatField()


class Discount(models.Model):
    _user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    _user_point = models.ForeignKey(PointCount,on_delete=models.CASCADE)
    _discount = models.FloatField()



#TO DO


#creating PointsCounter instance
#@receiver(post_save,sender=User)
#def create_points_counter(sender,instance,created,**kwargs):
 #   if created:
  #      PointCount.objects.create(user_id=instance,points=0)

#creating discount table instance
#@receiver(post_save,sender=User)
#def create_points_counter(sender,instance,created,**kwargs):
 #   if created:
  #      Discount.objects.create(user_point=instance,discount=0)

#update