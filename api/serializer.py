from rest_framework import serializers
from rest_framework.response import Response
from onlinestore.models import Sneakers


class SneakersSerializer(serializers.ModelSerializer):
    some_comment = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='comment_text'
    )

    class Meta:
        model = Sneakers
        fields = "__all__"
    # name = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=15, decimal_places=2)
    # slug = serializers.CharField(max_length=100)
    # available = serializers.BooleanField(default=True)
    # id = serializers.IntegerField()
    # description = serializers.CharField()
    # img = serializers.ImageField(read_only=True)
    #
    # def create(self, validated_data):
    #     return Sneakers.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.price = validated_data.get("price", instance.price)
    #     instance.slug = validated_data.get("slug", instance.slug)
    #     instance.available = validated_data.get("available", instance.available)
    #     instance.id = validated_data.get("id", instance.id)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.img = validated_data.get("img", instance.img)
    #     instance.save()
    #     return instance
