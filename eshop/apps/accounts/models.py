from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save

# Create your models here.
import datetime
from django.db.models import Sum
from ..orders.models import Order

#class OrderPreviousStatus(models.Model):
 #   order=models.OneToOneField(Order,on_delete='cascade')
  #  status = models.CharField(max_length=20,choices=)

class PointCount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    points = models.FloatField()

#В зависимости от накопленных за определенное время денег у пользователя будет та или иная скидка
class Discount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pointcount = models.OneToOneField(PointCount,on_delete=models.CASCADE)
    discount = models.FloatField(default=0.05) #range 0-1. 0.05=5%
    prev_count = models.FloatField(default=0) #points collected previous month

#Чтобы пользователи были ещё больше замотивированы совершать новые покупки,
#у людей будет высвечиваться то, в каком перцентиле по деньгам, потраченным на покупки, они находятся
#То есть, если вы потратили больше, чем 90% ппоользователей, то окно рейтинга покажет вам циферку 99
#Это добавит элемент соревновательности в ситсему
class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pointcount = models.OneToOneField(PointCount,on_delete=models.CASCADE)
    percentile=models.FloatField(default=100)

#TO DO


#creating PointsCounter instance
@receiver(post_save,sender=User)
def create_points_count(sender,instance,created,**kwargs):
    if created:
        #PointCount.objects.raw(f"INSERT VALUES({instance}, 0)")
        PointCount.objects.create(user=instance,points=0)


#creating discount table instance
@receiver(post_save,sender=PointCount)
def create_discount(sender,instance,created,**kwargs):
    if created:
        Discount.objects.create(pointcount=instance,user=instance.user,discount=0.05)

#Creating rating table model
@receiver(post_save,sender=PointCount)
def create_rating(sender,instance,created,**kwargs):
    if created:
        Rating.objects.create(pointcount=instance,user=instance.user)


#UPDATING MODELS (TO DO)

#update points
#Эта функция будет проверена и раскоменчена, когда у меня будет возможность создавать заказы
#через админку.

#@receiver(pre_save,sender=Order)
#def update_from_orders(sender,instance,created,**kwargs):
 #   if not created:
  #      for item in iter(kwargs.get("updated_fields")):
   #         if item=='ORDER_TYPE':
    #            old_instance=Order.objects.get(instance.id)
     #           old_status=old_instance.status
      #          if datetime.dtatime.now().day>14:
                    #if old_status=='PAID' and instance.status=='CANCELLED':
                     #   user_count = PointCount.objects.get(user=instance.user)
                      #  user_count.points-=instance.price
                       # user_count.save()
                    #elif instance.status=='PAID':
                     #   user_count = PointCount.objects.get(user=instance.user)
                      #  user_count.points+=instance.price
                       # user_count.save()
                #else:
                 #   user_discount = Discount.objects.get(user=instance.user)
                  #  if old_status=='PAID' and instance.status=='CANCELLED':
                   #     user_discount.prev_count-=instance.price
                    #    user_discount.save()
                   # elif instance.status=='PAID':
                    #    user_count = PointCount.objects.get(user=instance.user)
                     #   user_count.points+=instance.price
                      #  user_count.save()
    #else:
     #   if instance.status=='PAID':
      #      user_count = PointCount.objects.get(user=instance.user)
       #     user_count+=instance.price






