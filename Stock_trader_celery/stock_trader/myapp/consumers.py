import json

from asgiref.sync import async_to_sync,sync_to_async
from channels.generic.websocket import WebsocketConsumer
from urllib.parse import parse_qs
from django_celery_beat.models import PeriodicTask,IntervalSchedule

class StockConsumer(WebsocketConsumer):
    @sync_to_async
    def addToCelerybeat(self,stockpicker):
        task=PeriodicTask.objects.filter(name="every-10-seconds")
        if len(task>0):
            task=task.first()
            args=json.loads(task.args)
            args=args[0]

            for x in stockpicker:
                if x not in args:
                    args.append(x)
            task.args=json.dumps([args])
            task.save()

        else:
            schedule,created=IntervalSchedule.objects.get_or_create(every=10,period=IntervalSchedule.SECONDS)
            task=PeriodicTask.objects.create(interval=schedule,name='every-10-seconds',task='myapp.tasks.update_stock',args=json.dumps([stockpicker]))


    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"stock_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, 
            self.channel_name
        )
       
       # Parse queryString
        query_parmas=parse_qs(self.scope['queryString'].decode())
        print(query_parmas)

        stockpicker= query_parmas['stockpicker']


        # add to the celery beat

        self.addToCelerybeat(stockpicker)
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "send_update", "message": message}
        )

    # Receive message from room group
    def send_stock_update(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({message}))