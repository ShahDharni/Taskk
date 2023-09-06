from rest_framework import serializers
from .models import HackernewsId

class NewsIDserializer(serializers.Serializer):

    class Meta:
        model=HackernewsId
        fields=("hackernews",)