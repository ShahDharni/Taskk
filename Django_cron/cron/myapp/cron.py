from django_cron import CronJobBase,Schedule
import requests
from .models import HackernewsId
from rest_framework import status
from django.http import HttpResponse

class MyJobCron(CronJobBase):
    RUN_EVERY_MINUTE=1  ## every 5 minutes
    REACH_AFTER_FAILURE_MINUTE=1
    schedule=Schedule(run_every_mins=RUN_EVERY_MINUTE,retry_after_failure_mins=REACH_AFTER_FAILURE_MINUTE)
    code='myapp.my_cron_job'

    def do(self):
        NEWS_URL='https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty' # external endpoints that returns the latest 5 ids
        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL,headers=headers)
        result = response.text.split(',')[1:len(response.text.split(','))-2]  # to trim the last element
        last = response.text.split(',')[-1]              #got this from API " 499287535 ] /n" --> reshaped to that below
        result.insert(len(result), last.strip().split()[0]) # "499287535"

        news = 400 # 100 downward/latest
        res = [int(id.strip()) for id in result[news+1:news+6]] # list comprehension

        for id in res:
            news_id = HackernewsId(hackernews=id)
            news_id.save()


