
import socketio

from .sock_server import sio

application = socketio.ASGIApp(sio)