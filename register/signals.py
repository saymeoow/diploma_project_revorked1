from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=User)
def user_create(**kwargs):
    instance = kwargs['instance']
    print(f'Пользователь {instance.username} создан.\n'
          f'email пользователя - {instance.email}\n'
          f'id пользователя - {instance.id}')


@receiver(post_delete, sender=User)
def user_delete(**kwargs):
    instance = kwargs['instance']
    print(f'Пользователь {instance.username} был удален.\n'
          f'email пользователя - {instance.email}\n'
          f'id пользователя - {instance.id}')
