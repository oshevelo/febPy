from django.db import models
from django.utils.translation import gettext_lazy as _

class Shipments(models.Model):
    userID = models.ForeignKey(UserID, on_delete=models.PROTECT)

    class DeliveryCompany(models.TextChoices):
        NEWPOST = 'NP', _('New Post')
        UKRPOST = 'UkrP', _('Ukr Post')
        MEEST = 'MT', _('Meest')
        JUSTIN = 'JN', _('Justin')
    delivery_company = models.CharField(
        max_length=10,
        choices=DeliveryCompany.choices,
        default=''
    )

    delivery_office_number = models.IntegerField(default='')  # как подтянуть список отделений доставки?
    addressee = models.BooleanField(default=False, help_text='Я получатель')

    class Delivery(models.TextChoices):
        PICKUP = 'PickUp', _('Pick-up from our stores')
        PICKUP_DELIV_DEP = 'PickUpDelivDepartment', _('Pick-up from delivery department')
        COURIER = 'Courier', _('Courier')
    delivery = models.CharField(
        max_length=32,
        choices=Delivery.choices,
        default=''
    )

    class Status(models.TextChoices):                        # от куда должны обновляться статусы доставки?
        AWAITING_SHIPMENT = 'AwaitingShipment', _('Awaiting Shipment')
        IN_DELIVERY_SERVICE = 'InDelivery', _('In Delivery Service')
        ON_THE_WAY = 'OnTheWay', _('On the way')
        ON_DEPARTMENT = 'OnDepartment', _('Order on delivery department')
        RECEIVED = 'Received', _('Received')
    status = models.CharField(
        max_length=32,
        choices=Status.choices,
        default=Status.AWAITING_SHIPMENT
    )
    comment = models.CharField(max_length=200)
