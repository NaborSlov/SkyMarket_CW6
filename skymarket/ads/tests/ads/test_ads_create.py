import pytest


@pytest.mark.django_db
def test_create_ads(user_client, user_api):
    data = {
        "title": "test title",
        "price": 1000,
        "description": "test description"
    }

    response = user_client.post("/api/ads/", data)

    expected_response = {
        "pk": response.data.get("pk"),
        "image": None,
        "title": "test title",
        "price": 1000,
        "phone": "+79224846016",
        "description": "test description",
        "author_first_name": "test name",
        "author_last_name": "test last_name",
        "author_id": user_api.pk
    }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_is_authorization(client):
    data = {
        "title": "test title",
        "price": 1000,
        "description": "test description"
    }

    response = client.post(f"/api/ads/", data)

    assert response.status_code == 401
