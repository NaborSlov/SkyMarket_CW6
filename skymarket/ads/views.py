from rest_framework import pagination, viewsets

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = AdDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
