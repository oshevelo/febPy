from django.db import models

class Product(models.Model):
    product_id = models.IntegerField(max_length=200)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    amount_in_stock = models.IntegerField()
    image = models.ForeingKey(Gallery)
    category = models.ForeignKey(Catalog)

    def __str__(self):
        return self.product_name

class Сomments(models.Model):
    product_id = models.ForeignKey(Product, verbose_name="Product")
    product_name = models.ForeignKey(Product, verbose_name="product_name")
    user = models.ForeignKey(UserProfiles)
    comments = models.TextField()
    product_rating = models.CharField()
    pub_date = models.DateTimeField('date published')

class Catalog(Product):
    product_id = models.ForeignKey(Product, verbose_name="Product")
    product_name = models.ForeignKey(Product, verbose_name="product_name")
    category = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
# manufacturer = models.ForeignKey(Manufacturer, verbose_name=_("Manufacturer"), )

