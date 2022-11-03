import pytest

from ads.models import Ad


@pytest.mark.django_db
def test_ads_delete(user_client, user_api):
    data = {
        "title": "test title patch",
        "price": 2000,
        "description": "test description patch",
        "author_id": user_api.pk
    }

    ad = Ad.objects.create(**data)

    response = user_client.delete(f"/api/ads/{ad.pk}/")

    assert response.status_code == 204


@pytest.mark.django_db
def test_ads_admin_delete(api_admin_client, ad):
    response = api_admin_client.delete(f"/api/ads/{ad.pk}/")
    assert response.status_code == 204
