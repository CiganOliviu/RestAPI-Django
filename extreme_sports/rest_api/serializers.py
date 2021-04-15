from .models import *
from rest_framework import serializers


class ExtremeSportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtremeSport
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class RegionsSerializer(serializers.ModelSerializer):

    country = CountrySerializer(read_only=True)

    class Meta:
        model = Region
        fields = '__all__'


class LocationsSerializer(serializers.ModelSerializer):

    regions = RegionsSerializer(read_only=True, many=True)

    class Meta:
        model = Location
        fields = '__all__'


    def to_representation(self, instance):

        rep_sports = super().to_representation(instance)
        rep_sports["sports"] = ExtremeSportsSerializer(instance.sports.all(), many=True).data

        return rep_sports

