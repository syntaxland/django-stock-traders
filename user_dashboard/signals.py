# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from channels.layers import get_channel_layer
# from .models import TraderData
# from .consumers import TraderDataConsumer

# @receiver(post_save, sender=TraderData)
# def send_trader_data_to_consumers(sender, instance, created, **kwargs):
#     if created:
#         channel_layer = get_channel_layer()
#         data = TraderDataConsumer.get_latest_trader_data()

#         channel_layer.group_send(
#             'trader_data_group',
#             {
#                 'type': 'send_trader_data',
#                 'data': data
#             }
#         )
