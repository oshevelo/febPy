from django.db import models
from django.db import product

# Create your models here.#


#Image model
class Image(models.Model):
    name = models.CharField(max_length=30)
    descrption = models.TextField(max_length=1000)
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL,
                                null=True, blank=True, verbose_name='Product')
    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    
    time_posted = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

# Декоратор обновления онлайн
    @classmethod
    def update_image(cls, id, name,description , product, category):
        update = cls.objects.filter(id=id).update(name=name, description=description, product=product)
        return update

# Декоратор получения
    @classmethod
    def get_image_by_id(cls, id):
        image_id = cls.objects.filter(id=id).all()
        return image_id

# Декоратор поиска 
    @classmethod
    def search_image(cls,product):
        images = Image.objects.filter(product__name__contains=product)
        return images

# Декоратор фильтрации по product
    @classmethod
    def filter_by_productcls(cls,product):
        image_product = cls.objects.filter(product=product).all()
        return image_product


    def __str__(self):
        return self.name

