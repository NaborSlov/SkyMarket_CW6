import pytest

from ads.serializers import AdListSerializer
from factorys import AdFactory


@pytest.mark.django_db
def test_list_ads(client):
    ads = AdFactory.create_batch(3)

    expected_response = {
        "count": 3,
        "next": None,
        "previous": None,
        "results": AdListSerializer(ads, many=True).data[::-1]
    }

    response = client.get("/api/ads/")

    assert response.status_code == 200
    assert response.data == expected_response
