from typing import List

from rest_framework import serializers

from ads.models import Comment, Ad


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()  # поле с работой от метода
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)  # получения значения из связанного поля
    author_image = serializers.ImageField(source="author.image", read_only=True)

    def get_author_first_name(self, obj):  # get_* и название MethodFild. В obj передается полученный объект из базы данных
        return obj.author.first_name

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


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", 'image', 'title', 'price', 'description']


class AdSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    phone = serializers.CharField(source="author.phone", read_only=True)

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

