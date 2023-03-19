import socket
from .base import *

ip = socket.gethostbyname(socket.gethostname())
ip_host = '80.78.246.159'

if ip == ip_host:
    from .production import *
else:
    from .developer import *
