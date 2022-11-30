import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

#application = get_asgi_application()
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter

from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter( {
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack( URLRouter( chat.routing.websocket_urlpatterns ) ),
} )