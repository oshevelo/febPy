from django.db import models
from django.utils.translation import gettext_lazy as _


class Shipments(models.Model):
    NEWPOST = 'NP'
    UKRPOST = 'UkrP'
    MEEST = 'MT'
    JUSTIN = 'JN'
    DELIVERY_COMPANY =[
        (NEWPOST, 'New Post'),
        (UKRPOST, 'Ukr Post'),
        (MEEST, 'Meest'),
        (JUSTIN,'Justin'),
    ]
    delivery_company = models.CharField(max_length=10, choices=DELIVERY_COMPANY, default='')
    #orderID = models.ForeignKey(Order, on_delete=models.PROTECT)
    delivery_office_number = models.IntegerField(default='')  # как подтянуть список отделений доставки?
    addressee_first_name = models.CharField(max_length=32)
    addressee_last_name = models.CharField(max_length=32)
    addressee_phone = models.CharField(max_length=10)

    PICKUP = 'PickUp'
    PICKUP_DELIV_DEP = 'PickUpDelivDepartment'
    COURIER = 'Courier'
    DELIVERY_METHOD=[
        (PICKUP, 'Pick-up from our stores'),
        (PICKUP_DELIV_DEP, 'Pick-up from delivery department'),
        (COURIER, 'Courier')
    ]
    delivery = models.CharField(max_length=32, choices=DELIVERY_METHOD,default='')

    AWAITING_SHIPMENT = 'AwaitingShipment'                       # от куда должны обновляться статусы доставки?
    IN_DELIVERY_SERVICE = 'InDelivery'
    ON_THE_WAY = 'OnTheWay'
    ON_DEPARTMENT = 'OnDepartment'
    RECEIVED = 'Received'
    STATUS=[
        (AWAITING_SHIPMENT, 'Awaiting Shipment'),
        (IN_DELIVERY_SERVICE, 'In Delivery Service'),
        (ON_THE_WAY, 'On the way'),
        (ON_DEPARTMENT, 'Order on delivery department'),
        (RECEIVED, 'Received'),
    ]
    status = models.CharField(max_length=32, choices=STATUS, default=AWAITING_SHIPMENT)
    comment = models.CharField(max_length=200)
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
