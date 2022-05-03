import json
from random import randint
from asyncio import sleep

from django.contrib import messages
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

class UpdateNotifConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "testRoom"
        self.room_group_name = "testGroupRoom"

        await self.channel_layer.group_add("testGroupRoom", self.channel_name)
        print(self.room_group_name)
        print(self.channel_name)
        await self.accept()
        
        #for i in range(1000):
         #   await self.send(json.dumps({'value': randint(0, 100)}))
          #  await sleep(2)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("testGroupRoom", self.channel_name)

    async def receive(self, text_data):
        print("new post")
        print(text_data)
        
        #await self.channel_layer.group_send(self.group_name, json.dumps({'value': text_data}))
        #await self.send(json.dumps({'value': text_data}))
        text_data_json = json.loads(text_data)
        message = text_data_json['value']

        await self.channel_layer.group_send(
                "testGroupRoom",
                {
                    'type': 'chat_message',
                    'value': message
        })

    async def chat_message(self, event):
        message = event['value']
        
        await self.send(text_data=json.dumps({
            'value': message
        }))
