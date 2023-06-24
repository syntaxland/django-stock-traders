"""
ASGI config for trader_dashboard project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trader_dashboard.settings')

application = get_asgi_application()


# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from trader_dashboard.routing import websocket_urlpatterns

# application = ProtocolTypeRouter(
#     {
#         'http': get_asgi_application(),
#         'websocket': URLRouter(websocket_urlpatterns),
#     }
# )
