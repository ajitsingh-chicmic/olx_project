
import os
import django
from django.core.asgi import get_asgi_application
# Set up Django first
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'olx.settings')
django.setup()

# Now you can import modules that rely on Django models
from chatapp.sock_server import sio
import socketio

# Initialize ASGI application
django_asgi_app=get_asgi_application()
application = socketio.ASGIApp(sio,django_asgi_app,)