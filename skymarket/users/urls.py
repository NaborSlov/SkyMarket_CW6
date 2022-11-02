from django.urls import include, path

# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этого рекомендуется использовать SimpleRouter

urlpatterns = [
    path("", include("djoser.urls")),
]
