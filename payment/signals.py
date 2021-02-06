from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Payment


@receiver(post_save, sender=Payment)
def update_on_save(sender, instance, created, **kwargs):
    """ Update order total on lineitem update/create """
    print("siganls are working")
    instance.update_total()


@receiver(post_delete, sender=Payment)
def update_on_delete(sender, instance, **kwargs):
    """ Update order total on lineitem update/create """
    #instance.payment.update_total()
    pass