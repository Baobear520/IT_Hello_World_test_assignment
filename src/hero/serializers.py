from rest_framework import serializers
from .models import *


class PowerStatsSerializer(serializers.Serializer):
    """
    Serializer for PowerStats model
    includes methods to parse integer/null values
    """
    intelligence = serializers.IntegerField(required=False, allow_null=True, default=0)
    strength = serializers.IntegerField(required=False, allow_null=True, default=0)
    speed = serializers.IntegerField(required=False, allow_null=True, default=0)
    durability = serializers.IntegerField(required=False, allow_null=True, default=0)
    power = serializers.IntegerField(required=False, allow_null=True, default=0)
    combat = serializers.IntegerField(required=False, allow_null=True, default=0)

    def to_internal_value(self, data):
        # Convert 'null' strings to None for proper handling
        for key in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']:
            if key in data and data[key] in ['null', '']:
                data[key] = 0
        return super().to_internal_value(data)

    def to_representation(self, instance):
        # Ensure all fields are present in the output
        ret = super().to_representation(instance)
        for field in ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']:
            if field not in ret or ret[field] is None:
                ret[field] = 0
        return ret

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





