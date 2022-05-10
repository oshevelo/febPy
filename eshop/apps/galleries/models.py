from django.db import models
from django.core.files import File ## Для хранения в локальном каталоге
import datetime as dt

# Create your models here.#


# АЛЕКС не хватает информации по рабботе с файловой системой !!!!!!! #




#Category model
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    #Method for updating category
    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id=id).update(location_name = name)

    def __str__(self):
        return self.category_name


#Location model
class Location(models.Model):
    location_name = models.CharField(max_length=100)


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    #Method for updating location
    @classmethod
    def update_location(cls,id,name):
        cls.objects.filter(id=id).update(location_name = name)

    def __str__(self):
        return self.location_name

#Image model
class Image(models.Model):
    name = models.CharField(max_length=30)
    descrption = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    ## Модель хранения изображения image = ТУТ должна быть ссылка на каталог хранени, точнее файла с изображением ????????!!!!!!
    time_posted = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

# Декоратор обновления онлайн
    @classmethod
    def update_image(cls, id ,name,description , location, category):
        update = cls.objects.filter(id = id).update(name = name,description=description,location= location,category=category)
        return update

# Декоратор получения
    @classmethod
    def get_image_by_id(cls,id):
        image_id = cls.objects.filter(id = id).all()
        return image_id

# Декоратор поиска
    @classmethod
    def search_image(cls,category):
        images = Image.objects.filter(category__name__contains=category)
        return images

# Декоратор фильтрации по локации
    @classmethod
    def filter_by_location(cls,location):
        image_location = cls.objects.filter(location=location).all()
        return image_location


    def __str__(self):
        return self.name

