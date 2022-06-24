from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.products.models import Product
from eshop.settings import QUANTITY_LIMIT, TOTAL_PRICE_LIMIT


class Cart(models.Model):
    """ CART """
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='User')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return f'Cart: user - {self.user}'

    """ CART TOTAL PRICE """
    @property
    def total_price(self):
        return sum([
            item.product.price * item.quantity for item in self.cart_items.all()
            if item.cart_item_is_available
        ])

    """ CHECK TOTAL PRICE """
    def validate_total_price(self):
        if self.total_price > TOTAL_PRICE_LIMIT:
            raise ValidationError(
                _('Total price exceeded'),
                params={'value': TOTAL_PRICE_LIMIT}
            )
        return self.total_price

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class CartItem(models.Model):
    """ CART ITEM """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                null=True, blank=True, verbose_name='Product')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Cart', related_name='cart_items')
    quantity = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(
            limit_value=1,
            message='Quantity must be greater then: 1'
        )]
    )

    def __str__(self):
        return f'Product: {self.product} - quantity: {self.quantity}'

    """ CART ITEM STATUS """
    @property
    def cart_item_is_available(self):
        return self.quantity <= self.product.amount_in_stock

    @property
    def cost_product(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'
        unique_together = (('product', 'cart'),)


