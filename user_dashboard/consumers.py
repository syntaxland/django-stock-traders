import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import TraderData

class TraderDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'trader_data_group'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_trader_data(self, event):
        data = event['data']
        await self.send(text_data=json.dumps(data))

    @staticmethod
    def get_latest_trader_data():
        trader_data = TraderData.objects.last()
        data = {
            'trader': trader_data.trader,
            'profit_loss': float(trader_data.profit_loss),
            'timestamp': str(trader_data.timestamp)
        }
        return data
