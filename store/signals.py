from .models import Order, OrderTicket
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


@receiver(pre_save, sender=Order)
def create_order_ticket(sender, instance, **kwargs):
    if instance.id:
        previous = Order.objects.get(id=instance.id)
        if previous.order_status != instance.order_status:
            order_ticket = OrderTicket(customer=instance.customer,
                                       order=instance,
                                       message=instance.order_status,
                                       type=1)
            order_ticket.save()
