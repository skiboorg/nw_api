import json
from pytils.translit import slugify
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from .models import *
from bs4 import BeautifulSoup
import requests
import shutil
import  os
class ParceMap(APIView):
    def get(self,request):

        for tile in range(0,1):
            print(tile)
            os.mkdir(f'media/map/{tile}')
            for y in range(1, 3):
                for x in range(0, 70):
                    print('y=', y)
                    print('x=', x)
                    url = f'https://newworldfans.com/tiles/{tile}/map_y-{y}_x{x}.jpg'

                    responce = requests.get(url, stream=True)
                    print('responce.status_code=', responce.status_code)
                    if responce.status_code == 200:
                        with open(f'media/map/{tile}/map_y-{y}_x{x}.jpg', 'wb') as out_file:
                            shutil.copyfileobj(responce.raw, out_file)

        return Response(status=200)
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