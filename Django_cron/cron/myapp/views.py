from django.shortcuts import render
from .serializers import NewsIDserializer
from .models import HackernewsId
import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

# Create your views here.
class News_Ids(APIView):
    permission_classes=[AllowAny,]

    def get(self,request,format=None):
        NEWS_URL='https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty' # external endpoints that returns the latest 5 ids
        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL,headers=headers)
        result = response.text.split(',')[1:len(response.text.split(','))-2]  # to trim the last element
        last = response.text.split(',')[-1]              #got this from API " 499287535 ] /n" --> reshaped to that below
        result.insert(len(result), last.strip().split()[0]) # "499287535"

        res = [int(id.strip()) for id in result] # list comprehension
        return Response(res,status=status.HTTP_200_OK)


class NewsId(APIView):
    permission_classes=[AllowAny,]

    def get_data_from_API(self):  #"""
    #         This helps to return 
    #         formatted data fetched from endpoint provided
    #         using request.
    #     """
    # latest = HackerNewsID.objects.all()[len(HackerNewsID.objects.all())-1].hackernews # getting latest id from db

        result=[]
        half=0
        total=len(HackernewsId.objects.all()) # getting the total ids from db

        if total %2 ==0:
            half=(len(HackernewsId.objects.all())/2) 
        else:
            half=(len(HackernewsId.objects.all())/2) + 1

        ids=HackernewsId.objects.all()[:half] # slicing ids to get the last half

        for id in ids:
            NEWS_URL=f'https://hacker-news.firebaseio.com/v0/item/{str(id)}.json?print=pretty' # external endpoints that returns the latest 5 ids
            headers = {'user-agent': 'quickcheck/0.0.1'}
            response = requests.get(NEWS_URL,headers=headers) 
            data=json.loads(response.text)
            result.append(data)
        return result

      
    def get(self, request, format=None):
        return Response(self.get_data_from_API(),status=status.HTTP_201_CREATED)