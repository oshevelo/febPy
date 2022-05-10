from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    """ CART """
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='User')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return f'Cart: {self.user}'

    """ CART TOTAL PRICE """
    @property
    def total_price(self):
        return sum([item.product.price * item.quantity for item in self.cart_items.all()])

    """ CHECK TOTAL PRICE """
    def validate_total_price(self, limit_price=100000):
        if self.total_price > limit_price:
            raise ValidationError(
                _('Limited total cost in cart: %(value)s'),
                params={'value': limit_price}
            )

    """ CHECK QUANTITY PRODUCT IN CART """
    def validate_quantity_product_in_cart(self, limit_quantity=10):
        if len(list(self.cart_items.all())) > limit_quantity:
            raise ValidationError(
                _('Limited quantity products in cart: %(value)s'),
                params={'value': limit_quantity}
            )

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class CartItem(models.Model):
    """ CART ITEM """
    # product = models.ForeignKey('products.Product', on_delete=models.SET_NULL,
    #                             null=True, blank=True, verbose_name='Product')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Cart', related_name='cart_items')
    quantity = models.IntegerField(default=1,)

    def __str__(self):
        return f'Cart item: {self.cart}'

    """ CHECK QUANTITY PRODUCT """
    def validate_quantity_product(self):
        if self.quantity > self.product.quantity:
            raise ValidationError(
                _('Product is available: %(value)s'),
                params={'value': self.product.quantity}
            )
        elif self.quantity < 1:
            raise ValidationError(
                _('Quantity must be greater then: %(value)s'),
                params={'value': 1}
            )

    @property
    def cost_product(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'

