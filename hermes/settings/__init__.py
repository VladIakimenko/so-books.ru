import socket
from .base import *

ip = socket.gethostbyname(socket.gethostname())
ip_hosts = ['80.78.246.159']

if ip in ip_hosts:
    from .production import *
else:
    from .developer import *
