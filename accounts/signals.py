from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import *

@receiver(post_save, sender=User)
def create_customer (sender, instance, created, **kwargs) :
    if created:
        group = Group.objects.get(name = "Customer")
        instance.groups.add(group)

        Customer.objects.create(user=instance)
     

@receiver(post_save, sender=User)
def update_customer (sender, instance, created, **kwargs):
     if created ==False:
        instance.customer.save()
 
  