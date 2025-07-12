# core/routing.py

from django.urls import re_path
from core.consumers.terminal import TerminalConsumer

websocket_urlpatterns = [
    re_path(r"ws/terminal/(?P<project_id>[\w-]+)/$", TerminalConsumer.as_asgi()),
]
