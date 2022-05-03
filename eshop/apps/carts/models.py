from django.db import models


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='User')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return f'{self.user}'

    @property
    def total_price(self):
        result_list = [item.product.price * item.quantity for item in self.cartitem_set.all()]
        return sum(result_list)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class CartItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, verbose_name='Product')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Cart')
    quantity = models.IntegerField(default=1)


    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'
