# core/consumers/terminal.py

from channels.generic.websocket import AsyncWebsocketConsumer
from core.terminal.core import TerminalProcess
from core.terminal.utils import clean_terminal_output  # Optional
import asyncio


class TerminalConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.project_id = self.scope["url_route"]["kwargs"]["project_id"]
        cwd = f"user_projects/{self.project_id}"

        self.term = TerminalProcess(
            cwd=cwd, on_output_async=self.send_output, loop=asyncio.get_event_loop()
        )

    async def receive(self, text_data):
        self.term.write(text_data)

    async def disconnect(self, code):
        self.term.stop()

    async def send_output(self, data):
        clean_output = clean_terminal_output(data)
        await self.send(text_data=clean_output)
