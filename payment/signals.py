from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import TicketsPayment


@receiver(post_save, sender=TicketsPayment)
def update_on_save(sender, instance, created, **kwargs):
    """ Update order total on lineitem update/create """
    instance.payment.update_total()


@receiver(post_delete, sender=TicketsPayment)
def update_on_delete(sender, instance, **kwargs):
    """ Update order total on lineitem update/create """
    instance.payment.update_total()
