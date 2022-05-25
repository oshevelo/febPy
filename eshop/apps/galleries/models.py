from django.db import models
#from django.db import product

# Create your models here.#


#Image model
class Image(models.Model):
#    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL,
#                                null=True, blank=True, verbose_name='Product', default='NULL')
    name = models.CharField(max_length=30, default='NULL')
    descrption = models.TextField(max_length=1000, default='NULL')

    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='NULL')

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

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

# Метод обновления онлайн
    @classmethod
    def update_image(cls, id, name, description, product, upload, size):
        update = cls.objects.filter(id=id).update(name=name, description=description,
                                                  product=product, upload=upload, size=size)
        return update

    def __str__(self):
        return self.name

