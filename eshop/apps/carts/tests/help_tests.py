from apps.products.models import Product
from apps.carts.models import Cart, CartItem


def create_product(sku='111', name='test', description='test descr', price=1000, amount_in_stock=5):
    product = Product.objects.create(
        sku=sku,
        name=name,
        description=description,
        price=price,
        amount_in_stock=amount_in_stock
    )
    return product


def create_cart_item(cart, product, quantity=2):
    cart_item = CartItem.objects.create(
        cart=cart,
        product=product,
        quantity=quantity
    )
    return cart_item
