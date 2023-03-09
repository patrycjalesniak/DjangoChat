import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Message, Chat
from django.contrib.auth.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_name = self.scope["url_route"]["kwargs"]["chat_name"]
        self.chat_group_name = f"chat_{self.chat_name}"

        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name,
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data["message"]
        username = data["username"]
        chat = data["chat"]

        await self.save_message(username, chat, message)
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username,
                "chat": chat,
            }
        )
    async def chat_message(self, event):
        message = event["message"]
        username = event ["username"]
        chat = event["chat"]

        await self.send(text_data = json.dumps({
            "message": message,
            "username" : username,
            "chat" : chat
        }))

    @sync_to_async
    def save_message(self, username, chat_slug, message ):
        user = User.objects.get(username=username)
        chat = Chat.objects.get(slug=chat_slug)

        Message.objects.create(user=user, chat=chat, content=message)


