import socket
from .base import *

ip = socket.gethostbyname(socket.gethostname())
ip_hosts = ['89.108.98.87', '80.78.246.159']

if ip in ip_hosts:
    from .production import *
else:
    from .developer import *
