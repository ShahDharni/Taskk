from django.shortcuts import render
from yahoo_fin.stock_info import *
from django.http import HttpResponse
import time
import queue
from threading import Thread   ## Threading is used to run multiple tasks or call function at the same time.


# Create your views here.


def stockPicker(request):
    # The Ticker class in yfinance provides various methods for accessing real-time stock data and information, such as the info method, which returns basic information about a stock symbol, and the recommendations method, which returns the latest analyst recommendations for the stock.
    stock_picker = tickers_nifty50()
    print(stock_picker)
    return render(request, 'myapp/stockpicker.html', {'stockpicker': stock_picker})


def stockTracker(request):
    # details=get_quote_table('TCS.NS')
    # print(details)
    # return render(request,'myapp/stocktracker.html')

    stockpicker = request.GET.getlist('stockpicker')
    print(stockpicker)
    data = {}
    available_stocks = tickers_nifty50()
    print('available_stocks',available_stocks)
    for i in stockpicker:
        print("i",i)
        if i in available_stocks:
            pass
        else:
            return HttpResponse("Error")
        
    n_threads=len(stockpicker)
    thread_list=[]
    que=queue.Queue()
    start=time.time()
    for i in range(n_threads):
        thread=Thread(target = lambda q, args1:q.put({stockpicker[i] : get_quote_table(args1)},args=(que,stockpicker[i])))
        thread_list.append(thread)
        thread_list[i].start()
        print("thread",thread)

    for thread in thread_list:
        thread.join()
    while not que.empty():
        result=queue.get()
        data.update(result)


# put(item) - This function is used to insert element to the queue -- put function in queue

    print(start)
    for i in stockpicker:
        details = get_quote_table(i)
        print('details',details)
        data.update({i:details},)
    end=time.time()
    time_taken= end - start
    print('time_taken',time_taken)
    print('end',end)
    print('data',data)
    return render(request, 'myapp/stocktracker.html',{'data':data,'room_name':'track'})


# The get_quote_table method can be used to extract the data found on the summary page of a stock. This method extracts financial data from the summary page of stock and returns it in the form of a dictionary.
