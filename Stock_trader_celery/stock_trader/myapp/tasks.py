from celery import shared_task
from django.shortcuts import render
from yahoo_fin.stock_info import *
from django.http import HttpResponse
import queue
from channels.layers import get_channel_layer
# Threading is used to run multiple tasks or call function at the same time.
from threading import Thread
import asyncio
import simplejson as json

@shared_task(bind=True)
def update_stock(self, stockpicker):

    data = {}
    available_stocks = tickers_nifty50()
    print('available_stocks', available_stocks)
    for i in stockpicker:
        print("i", i)
        if i in available_stocks:
            pass
        else:
            stockpicker.remove(i)

    n_threads = len(stockpicker)
    thread_list = []
    que = queue.Queue()
    for i in range(n_threads):
        thread = Thread(target=lambda q, args1: q.put(
            {stockpicker[i]:json.loads(json.dumps(get_quote_table(args1), ignore_nan=True))}, args=(que, stockpicker[i])))
        thread_list.append(thread)
        thread_list[i].start()
        print("thread", thread)

    for thread in thread_list:
        thread.join()
    while not que.empty():
        result = queue.get()
        data.update(result)

        # send data to group
        channel_layer = get_channel_layer()
        # asyncio is a library to write concurrent code using the async/await syntax
        loop = asyncio.new_event_loop
        asyncio.set_event_loop(loop)

        loop.run_until_complete(channel_layer.group_send('stock_tracker', {
            'type': 'send_update_stock',
            'message': data,
        }))
    return "done"



# put(item) - This function is used to insert element to the queue -- put function in queue

    # for i in stockpicker:
    #     details = get_quote_table(i)
    #     print('details',details)
    #     data.update({i:details})

    # print('data',data)
    # return render(request, 'myapp/stocktracker.html',{'data':data})
