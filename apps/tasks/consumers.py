from channels.generic.websocket import AsyncWebsocketConsumer
import json


class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def diconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Broadcast message to all connected clients
        await self.send(text_data=json.dumps({
            'message': message
        }))
