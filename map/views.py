import json
from pytils.translit import slugify
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from .models import *
from bs4 import BeautifulSoup
import requests


class ParcePoi(APIView):
    def get(self,request):
        url = 'https://newworldfans.com/api/v1/map/poi'
        responce = requests.get(url)
        # Poi.objects.create(image='images/poi/i.png')
        for i in responce.json():
            Poi.objects.create(name_en=i['name'],
                               image=f'images/poi/{i["icon_path"]}',
                               level=i['level'],
                               description=i['description'],
                               x_game=i['x_game'],
                               x_map=i['x_map'],
                               y_game=i['y_game'],
                               y_map=i['y_map'],
                               lat=i['lat'],
                               lng=i['lng'],
                               )

        return Response(status=200)

class ParceResource(APIView):
    def get(self,request):
        url = 'https://newworldfans.com/api/v1/map/resource'
        responce = requests.get(url)

        for i in responce.json():
            cat,create = ResourceCategory.objects.get_or_create(name_slug=i['category'])
            if create:
                cat.name_en=i['category'].replace('_',' ').capitalize()
                cat.name_slug=i['category']
                cat.image = f'images/resource/{i["category"]}.png'
                cat.save()
            Resource.objects.create(category=cat,
                                    lat=i['lat'],
                                    description=i['description'],
                                    lng=i['lng'],
                                    )
        return Response(status=200)

class GetPoi(generics.ListAPIView):
    serializer_class = PoiSerializer
    queryset = Poi.objects.all()

class GetResourse(generics.ListAPIView):
    serializer_class = ResourceTypeSerializer
    queryset = ResourceType.objects.all()