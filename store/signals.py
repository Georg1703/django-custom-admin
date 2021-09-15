from .models import Order, OrderTicket, OrderStatus
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


# @receiver(pre_save, sender=Order)
# def create_order_ticket(sender, instance, **kwargs):
#
#     try:
#         previous = sender.objects.get(id=instance.id)
#     except sender.DoesNotExist:
#         pass
#     else:
#         # print(previous.order_status, instance.order_status, '--------------')
#         if instance.placed == 1:
#             order_status = OrderStatus(name='placed')
#             instance.order_status = order_status
#             order_ticket = OrderTicket(customer=instance.customer,
#                                        order=instance,
#                                        message=instance.order_status,
#                                        type=1)
#             order_ticket.save()
