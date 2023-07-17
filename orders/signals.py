from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from .models import Order
from django.dispatch import receiver


@receiver(pre_save, sender=Order)
def order_prepare_to_create(**kwargs):
    print(f'Заказ готовится к созданию')


@receiver(post_save, sender=Order)
def order_create(**kwargs):
    instance = kwargs['instance']
    print(f'Заказ номер {instance.id} создан\n'
          f'статус оплаты - {instance.paid}')
