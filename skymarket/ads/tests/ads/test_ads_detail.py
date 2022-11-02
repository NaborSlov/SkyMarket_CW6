import pytest


@pytest.mark.django_db
def test_detail_ads(user_client, ad):
    expected_response = {
        "pk": ad.pk,
        "image": None,
        "title": "test title",
        "price": 1000,
        "phone": "+79993704028",
        "description": "test description",
        "author_first_name": "test name",
        "author_last_name": "test last_name",
        "author_id": ad.author.id
    }

    response = user_client.get(f"/api/ads/{ad.pk}/")

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_is_authorization(client, ad):
    response = client.get(f"/api/ads/{ad.pk}/")

    assert response.status_code == 401
