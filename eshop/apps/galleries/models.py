from django.db import models
from apps.products.models import Product
from django.contrib.auth.models import User

#Image model
class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                               verbose_name='Product', null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    descrption = models.TextField(max_length=1000, default='N/A')

    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='uploads/no_image.png')

    SMALL = 'SMALL'
    MEDIUM = 'MEDIUM'
    BIG = 'BIG'

    SIZE_CHOICE = [
        (SMALL, 'SMALL'),
        (MEDIUM, 'MEDIUM'),
        (BIG, 'BIG')
    ]
    size = models.CharField(max_length=30, choices=SIZE_CHOICE, default=SMALL)
    time_posted = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    editor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='image_editor')

# Метод обновления онлайн
    @classmethod
    def update_image(cls, id, name, description, product, upload, size):
        update = cls.objects.filter(id=id).update(name=name, description=description,
                                                  product=product, upload=upload, size=size)
        return update

    def __str__(self):
        return self.name
