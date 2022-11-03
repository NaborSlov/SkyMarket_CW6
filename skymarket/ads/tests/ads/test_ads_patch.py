import pytest

from ads.models import Ad


@pytest.mark.django_db
def test_patch_ads(user_client, user_api):
    data = {
        "title": "test title patch",
        "price": 2000,
        "description": "test description patch",
        "author_id": user_api.pk
    }

    ad = Ad.objects.create(**data)

    response = user_client.patch(f"/api/ads/{ad.pk}/", data)

    expected_response = {
        "pk": response.data.get("pk"),
        "image": None,
        "title": "test title patch",
        "price": 2000,
        "phone": "+79224846016",
        "description": "test description patch",
        "author_first_name": "test name",
        "author_last_name": "test last_name",
        "author_id": user_api.pk
    }

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_admin_patch_ads(api_admin_client, user_api):
    data = {
        "title": "test title patch",
        "price": 2000,
        "description": "test description patch",
        "author_id": user_api.pk
    }

    ad = Ad.objects.create(**data)

    response = api_admin_client.patch(f"/api/ads/{ad.pk}/", data)

    expected_response = {
        "pk": response.data.get("pk"),
        "image": None,
        "title": "test title patch",
        "price": 2000,
        "phone": "+79224846016",
        "description": "test description patch",
        "author_first_name": "test name",
        "author_last_name": "test last_name",
        "author_id": user_api.pk
    }

    assert response.status_code == 200
    assert response.data == expected_response


