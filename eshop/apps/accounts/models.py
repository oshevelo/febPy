from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class PointCount(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    points = models.FloatField()

#В зависимости от накопленных за определенное время денег у пользователя будет та или иная скидка
class Discount(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    user_points = models.ForeignKey(PointCount,on_delete=models.CASCADE)
    discount = models.FloatField(default=0.05)
    percent_to_pay = models.FloatField(default=0.95)

#Чтобы пользователи были ещё больше замотивированы совершать новые покупки,
#у людей будет высвечиваться то, в каком перцентиле по деньгам, потраченным на покупки, они находятся
#То есть, если вы потратили больше, чем 90% ппоользователей, то окно рейтинга покажет вам циферку 99
#Это добавит элемент соревновательности в ситсему
class Rating(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    user_points = models.ForeignKey(PointCount,on_delete=models.CASCADE)
    percentile=models.FloatField(default=100)

#TO DO


#creating PointsCounter instance
@receiver(post_save,sender=User)
def create_points_counter(sender,instance,created,**kwargs):
    if created:
        PointCount.objects.create(user_id=instance,points=0)

#creating discount table instance
@receiver(post_save,sender=PointCount)
def create_points_counter(sender,instance,created,**kwargs):
    if created:
        Discount.objects.create(user_points=instance,user_id=instance.user_id)

#Creating rating table model
@receiver(post_save,sender=PointCount)
def create_points_counter(sender,instance,created,**kwargs):
    if created:
        Rating.objects.create(user_points=instance,user_id=instance.user_id)


#UPDATING MODELS (TO DO)

#update points


#update

