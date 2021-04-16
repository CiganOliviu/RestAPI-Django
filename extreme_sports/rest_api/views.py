from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Location
from .serializers import LocationsSerializer, LocationsListerSerializer

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

class LocationsList(APIView):

    def get(self, request, format=None):

        locations = Location.objects.all()
        serializer = LocationsSerializer(locations, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = LocationsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def search_data(self, request, format=None):
        pass

class LocationDetail(APIView):

    def get_post(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = LocationsSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        locations = self.get_post(pk)
        serializer = LocationsSerializer(locations, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_post(pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class APILocations(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationsListerSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('sports__name', 'sports__period')
