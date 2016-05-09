from rest_framework import serializers

from .models import Advice, Cloth


class ClothSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    image_url = serializers.CharField()
    link = serializers.CharField()

    def create(self, validated_data):
        return Cloth.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.link = validated_data.get('link', instance.link)
        instance.save()
        return instance


class AdviceSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    clothes = ClothSerializer(many=True)

    def create(self, validated_data):
        return Advice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.clothes = validated_data.get('clothes', instance.clothes)
        instance.save()
        return instance
