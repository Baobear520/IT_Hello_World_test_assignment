
from django.conf import settings
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import *
from .scripts import fetch_data
from .serializers import HeroInputSerializer, RetrieveHeroListSerializer


class HeroListCreateView(ListCreateAPIView):
    queryset = Hero.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RetrieveHeroListSerializer
        return HeroInputSerializer  # Use input serializer for POST

    def create(self, request, *args, **kwargs):
        # Step 1: Validate user input
        input_serializer = HeroInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        name = input_serializer.validated_data['name']

        # Step 2: Fetch from third-party API
        hero_data_list, error, status_code = fetch_data(name,url=settings.API_BASE_URL,api_key=settings.API_KEY)
        if error:
            if status_code == 404:
                return Response(
                    {'detail': error},
                    status=status.HTTP_404_NOT_FOUND
                )
            elif status_code == 500:
                print(error)
                return Response(
                    {'detail': 'Service Unavailable'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        # Step 3: Validate API response
        output_serializer = RetrieveHeroListSerializer(data=hero_data_list, many=True)
        output_serializer.is_valid(raise_exception=True)

        # Step 4: Save to DB (expand as needed)
        heros_created = []
        for hero_data in output_serializer.validated_data:
            powerstats_data = hero_data.pop('powerstats')
            biography_data = hero_data.pop('biography')
            appearance_data = hero_data.pop('appearance')
            work_data = hero_data.pop('work')
            connections_data = hero_data.pop('connections')
            image_data = hero_data.pop('image')

            powerstats_object = PowerStats.objects.create(**powerstats_data)
            biography_object = Biography.objects.create(**biography_data)
            appearance_object = Appearance.objects.create(**appearance_data)
            work_object = Work.objects.create(**work_data)
            connections_object = Connections.objects.create(**connections_data)
            image_object = Image.objects.create(**image_data)
            hero = Hero.objects.create(
                name=hero_data['name'],
                powerstats=powerstats_object,
                biography=biography_object,
                appearance=appearance_object,
                work=work_object,
                connections=connections_object,
                image=image_object
            )
            heros_created.append(hero)

        data = [{'id': hero.id, 'name': hero.name} for hero in heros_created]

        # Step 5: Return serialized data
        return Response(data={'Heroes created': data}, status=status.HTTP_201_CREATED)



