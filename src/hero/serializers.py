from rest_framework import serializers
from .models import *


class PowerStatsSerializer(serializers.Serializer):
    """
    Serializer for PowerStats model
    includes methods to parse integer values in case of string values
    present in the response
    """
    intelligence = serializers.SerializerMethodField()
    strength = serializers.SerializerMethodField()
    speed = serializers.SerializerMethodField()
    durability = serializers.SerializerMethodField()
    power = serializers.SerializerMethodField()
    combat = serializers.SerializerMethodField()


    def get_intelligence(self, obj):
        return self._parse_int(obj.intelligence)

    def get_strength(self, obj):
        return self._parse_int(obj.strength)

    def get_speed(self, obj):
        return self._parse_int(obj.speed)

    def get_durability(self, obj):
        return self._parse_int(obj.durability)

    def get_power(self, obj):
        return self._parse_int(obj.power)

    def get_combat(self, obj):
        return self._parse_int(obj.combat)

    def _parse_int(self, value):
        try:
            return int(value)
        except (TypeError, ValueError):
            return None

class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        exclude = ('id',)

class AppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appearance
        exclude = ('id',)

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        exclude = ('id',)

class ConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connections
        exclude = ('id',)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ('id',)


class RetrieveHeroListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    powerstats = PowerStatsSerializer()
    biography = BiographySerializer()
    appearance = AppearanceSerializer()
    work = WorkSerializer()
    connections = ConnectionsSerializer()
    image = ImageSerializer()

class HeroInputSerializer(serializers.Serializer): #create
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def validate_name(self, name):
        # Remove extra spaces and capitalize each word
        normalized_name = '-'.join(word.capitalize() for word in name.strip().replace('-', ' ').split())
        print(normalized_name)
        if Hero.objects.filter(name=normalized_name).exists():
            raise serializers.ValidationError("Hero with this name already exists")
        return normalized_name





