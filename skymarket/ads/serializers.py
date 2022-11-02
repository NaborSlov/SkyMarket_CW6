from typing import List

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ads.models import Comment, Ad


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(max_length=50, read_only=True)
    author_last_name = serializers.CharField(max_length=50, read_only=True)
    author_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "pk",
            "text",
            "author_id",
            "created_at",
            "author_first_name",
            "author_last_name",
            "ad_id",
            "author_image"
        ]

    def get_fields(self):
        data = getattr(self, "instance", None)

        if isinstance(data, List):
            for obj in data:
                author = getattr(obj, 'author', None)

                obj.author_first_name = author.first_name
                obj.author_last_name = author.last_name
                obj.author_image = author.image
        elif data:
            author = getattr(data, 'author', None)

            self.instance.author_first_name = author.first_name
            self.instance.author_last_name = author.last_name
            self.instance.author_image = author.image

        return super().get_fields()


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", 'image', 'title', 'price', 'description']


class AdSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(max_length=50, read_only=True)
    author_last_name = serializers.CharField(max_length=50, read_only=True)
    phone = serializers.CharField(max_length=10, read_only=True)

    class Meta:
        model = Ad
        fields = [
            'pk',
            'image',
            'title',
            'price',
            'phone',
            'description',
            'author_first_name',
            'author_last_name',
            'author_id'
        ]

    def create(self, validated_data):
        ad = super().create(validated_data)

        ad.author_first_name = ad.author.first_name
        ad.author_last_name = ad.author.last_name
        ad.phone = ad.author.phone

        return ad

    def get_fields(self):
        author = getattr(self.instance, 'author', None)

        if author:
            self.instance.author_first_name = author.first_name
            self.instance.author_last_name = author.last_name
            self.instance.phone = author.phone

        return super().get_fields()
